"""
Title: pymonday
Author: Scott Murray
Version: 2.1.0
API Version 2024-01
"""

# IMPORT REQUIRED MODULES:
import os
import asyncio
import httpx
from time import sleep
from .columns import column_formats


# API ENDPOINTS:
monday_api_URL = 'https://api.monday.com/v2'
monday_file_URL = 'https://api.monday.com/v2/file'

# API RETRY STRATEGY:
MAX_RETRIES = 3

# GLOBAL VARIABLES
results = []
column_values = column_formats


class MondayAPIClient:
    ####################################################################################################################
    # ***INITIALIZER***
    ####################################################################################################################
    def __init__(self, api_key):
        """
        Client for the monday.com GraphQL API.
        """
        self.access_token = api_key

        self.session = httpx.Client()

        self.session.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "API-Version": "2023-10"}

    ####################################################################################################################
    # ***METHODS***
    ####################################################################################################################
    # HTTPX REQUESTS
    ####################################################################################################################
    def __send_post_request(self, payload):
        """
        API POST Request using HTTPX Session
        :param payload: Json query string
        :return: Json formatted Data from the HTTP response. Return None on API call failure.
        """
        for _ in range(MAX_RETRIES):
            response = self.session.post(url=monday_api_URL, json=payload, timeout=30.0)
            if response.status_code == 200:
                return response.json()
            print(response.content)
            sleep(5)

    ####################################################################################################################
    def __upload_file(self, payload, files):
        """
        API POST Request for file uploads.
        :param payload: JSON GraphQL query string.
        :param files: Files to be uploaded.
        :return: JSON response from API call.
        """
        file_headers = {'Authorization': self.access_token, "API-Version": "2024-01"}
        for _ in range(MAX_RETRIES):
            response = httpx.request(
                method="POST", url=monday_file_URL, data=payload, files=files, headers=file_headers)
            if response.status_code == 200:
                return response.json()
            print(response.content)
            sleep(5)

    ####################################################################################################################
    async def __async_post(self, payload):
        """
        Asynchronous API call to accelerate data retrieval and overcome I/O Bound Issues.
        :param payload: JSON GraphQL Query String.
        :return: Json formatted Data from the HTTP response. Return None on API call failure.
        """
        async with httpx.AsyncClient(headers=self.session.headers) as client:
            for _ in range(MAX_RETRIES):
                response = await client.post(url=monday_api_URL, json=payload, timeout=60)
                if response.status_code == 200:
                    results.append(response.json())
                    return
                print(response.content)
                sleep(5)

    ####################################################################################################################
    async def __column_task_handler(self, item_ids, columns):
        """
        Async task handler for column value retrieval.
        :param item_ids: UUID of the Item to retrieve column values for.
        :param columns: UUID of the columns values to retrieve.
        :return: Json formatted Data from the HTTP response. Return None on API call failure.
        """
        column_string = ""
        for column in columns:
            column_string = column_string + f"\"{column}\", "
        column_string = column_string[:-2]
        column_string = f"[{column_string}]"

        tasks = []
        for each_item in item_ids:
            query_string = f'''
            {{items(ids: {each_item}) {{id name parent_item{{id name}}column_values(ids: {column_string}) 
            {{id text value column{{id title}} 
            ... on MirrorValue{{display_value}} 
            ... on BoardRelationValue{{display_value linked_items{{id}}}}}}}}}}'''
            payload = {'query': query_string}
            tasks.append(self.__async_post(payload))
        await asyncio.gather(*tasks)

    ####################################################################################################################
    # BOARDS
    ####################################################################################################################
    def get_all_boards(self):
        """
        Get all boards from the platform.
        :return: Dictionary containing Board IDs and Board Names. Return None on API call failure.
        """
        query_string = f'''
        query {{boards(limit: 1000) {{name id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        board_data = response['data']['boards']
        return {item['id']: item['name'] for item in board_data}

    ####################################################################################################################
    def get_board_info(self, board_id):
        """
        Get the following information from a board: Name, ID, State, Permissions, Type, Workspace.
        :param board_id: UUID of the board.
        :return: Dictionary containing above values. Return None on API call failure.
        """
        query_string = f'''
        query {{boards (ids: {board_id}) {{name state id permissions board_kind workspace_id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        board_data = response['data']['boards'][0]
        return board_data

    ####################################################################################################################
    def get_board_groups(self, board_id):
        """
        Get all groups of a specific board.
        :param board_id: UUID of the board.
        :return: Dictionary containing Group IDs and Group Names. Return None on API call failure.
        """
        query_string = f'''
        query {{boards (ids: {board_id}) {{groups {{id title}}}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        group_data = response['data']['boards'][0]['groups']
        return {item['title']: item['id'] for item in group_data}

    ####################################################################################################################
    def get_board_from_item(self, item_id):
        """
        Get UUID of the board an item is on.
        :param item_id: UUID of the item.
        :return: Dictionary containing Board IDs and Board Names. Return None on API call failure.
        """
        query_string = f'''
        query {{items(ids: {item_id}){{board{{id name}}}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        board_data = response['data']['items'][0]['board']
        return board_data

    ####################################################################################################################
    def create_board(self, board_name, board_type, workspace_id):
        """
        Create a new board within a specific workspace.
        :param board_name: Required. The Name of the new board
        :param board_type: Required. Board Visibility. Options: public, private, share
        :param workspace_id: Required. UUID of the workspace to create the board in
        :return: UUID of newly created board. Return None on API call failure.
        """
        query_string = f'''mutation 
        {{create_board (board_name: "{board_name}", board_kind: {board_type}, workspace_id: {workspace_id}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        new_board = response['data']['create_board']['id']
        return new_board

    ####################################################################################################################
    def delete_board(self, board_id):
        """
        Delete a board.
        :param board_id: UUID of the board to delete.
        :return: ID of the board which was deleted. Return None on API call failure.
        """
        query_string = f'''mutation 
                {{delete_board (board_id: {board_id}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)
        if response:
            return response['data']['delete_board']['id']

    ####################################################################################################################
    def update_board_description(self, board_id, description):
        """
        Update the description of a specific board.
        :param board_id: UUID of the board to update.
        :param description: Text String to be used as the board description.
        :return: None
        """
        query_string = f'''mutation {{
        update_board(board_id: {board_id}, board_attribute: description, new_value: "{description}")}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if response:
            print(response['data'])

    ####################################################################################################################
    def archive_board(self, board_id):
        """
        Archive a board.
        :param board_id: UUID of the board to archive.
        :return: None
        """
        query_string = f'''mutation {{archive_board (board_id: {board_id}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if response:
            print(response)

    ####################################################################################################################
    # USERS
    ####################################################################################################################
    def get_all_users(self):
        """
        Get the names of all platform users and their UUIDs
        :return: Dictionary of item IDs and usernames. Return None on API call failure.
        """
        query_string = f'''query {{users(limit: 200) {{id name email phone country_code created_at last_activity}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        user_data = response['data']['users']
        return {item['id']: item['name'] for item in user_data}

    ####################################################################################################################
    def get_user_info(self, user_id):
        """
        Get all details of a specific user. One UUID permitted per query.
        :param user_id: UUID of the User.
        :return: Dictionary containing user specific information. Return None on API call failure.
        """
        query_string = f'''query {{
        users(ids: {user_id}) {{id name email phone country_code created_at last_activity}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        user_data = response['data']['users'][0]
        return user_data

    ####################################################################################################################
    def add_user_to_workspace(self, workspace_id, user_ids):
        """
        Add users to a workspace as subscribers.
        :param workspace_id: UUID of the workspace. Single Integer value.
        :param user_ids: UUIDs of the monday.com users to add. Should be a list of integers.
        :return: None.
        """
        query_string = f'''mutation {{
        add_users_to_workspace (workspace_id: {workspace_id}, user_ids: {user_ids}, kind: subscriber) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    def delete_user_from_workspace(self, workspace_id, user_ids):
        """
        Remove users from a workspace.
        :param workspace_id: UUID of the workspace. Single Integer value.
        :param user_ids: UUIDs of the monday.com users to remove. Should be a list of integers.
        :return: None.
        """
        query_string = f'''mutation {{
        delete_users_from_workspace (workspace_id: {workspace_id}, user_ids: {user_ids}, kind: subscriber) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    def add_user_to_board(self, board_id, user_ids):
        """
        Add users to a board as subscribers.
        :param board_id: UUID of the board. Single Integer value.
        :param user_ids: UUIDs of the users to add. Should be a list of integers.
        :return: None.
        """
        query_string = f'''mutation {{
        add_users_to_board (board_id: {board_id}, user_ids: {user_ids}, kind: subscriber) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    def remove_user_from_board(self, board_id, user_ids):
        """
        Remove users from a board as subscribers.
        :param board_id: UUID of the board. Single Integer value.
        :param user_ids: UUIDs of the users to remove. Should be a list of integers.
        :return: None.
        """
        query_string = f'''mutation {{
            delete_subscribers_from_board (board_id: {board_id}, user_ids: {user_ids}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    # WORKSPACES
    ####################################################################################################################
    def get_workspaces(self):
        """
        Get all monday.com workspaces
        :return: Dictionary of workspaces IDs and Names. Returns None on API call failure.
        """
        query_string = f'''query {{workspaces {{id name kind description}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        workspace_data = response['data']['workspaces']
        return workspace_data

    ####################################################################################################################
    # TEAMS
    ####################################################################################################################
    def get_teams(self):
        """
        Get Names and IDs of all teams.
        :return: Dictionary of IDs and Names. Return None on API call failure.
        """
        query_string = f'''{{teams {{name id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        team_data = response['data']['teams']
        teams = {item['id']: item['name'] for item in team_data}
        return teams

    ####################################################################################################################
    def get_team_members(self, team_ids):
        """
        Get ID, Name & Email of team members.
        :param team_ids: UUIDs of the Teams to be retrieved. List of integers.
        :return: Dictionary of Teams and member data. Return None on API call failure.
        """
        query_string = f'''{{teams (ids: {team_ids}){{name users {{name id email}}}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        member_data = response['data']['teams']
        team_dictionary = {item['name']: item['users'] for item in member_data}
        return team_dictionary

    ####################################################################################################################
    # GROUPS
    ####################################################################################################################
    def create_group(self, board_id, group_name):
        """
        Create a new group on a board at the top position.
        :param board_id: UUID of the board to create the item on.
        :param group_name: Name of the new group to be created.
        :return: UUID of the newly created group.
        """
        query_string = f'''mutation {{create_group (board_id: {board_id}, group_name: "{group_name}") {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['create_group']['id']

    ####################################################################################################################
    def delete_group(self, board_id, group_id):
        """
        Delete a group from a board.
        :param board_id: UUID of the board to delete the group from.
        :param group_id: UUID of the group to delete.
        :return: None
        """
        query_string = f'''mutation {{delete_group (board_id: {board_id}, group_id: "{group_id}") {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    def move_item_to_group(self, item_id, group_id):
        """
        Move an item from one group in a board to another.
        :param item_id: UUID of the item to move.
        :param group_id: UUID of the group to move the item to.
        :return: None.
        """
        query_string = f'''mutation {{move_item_to_group (item_id: {item_id}, group_id: "{group_id}") {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    # FOLDERS
    ####################################################################################################################
    def get_folders(self, workspace_id):
        """
        Get all folders in a workspace.
        :param workspace_id: UUID of the workspace.
        :return: Array of Dictionaries containing folder data. Return None on API call failure.
        """
        query_string = f'''query {{folders (workspace_ids: {workspace_id}) {{name id children {{id name}}}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['folders']

    ####################################################################################################################
    def create_folder(self, name, workspace_id, **kwargs):
        """
        Create a folder in a workspace. Pass keyword arguments to configure folder attributes. **Keywords must be passed
        exactly as defined below. Folder colors can be found here:
        https://asset.cloudinary.com/monday-platform-dev/3e39afb2309b512f4f53cc9173554d48
        :param name: The Folders name (Required)
        :param workspace_id: The unique identifier of the workspace to create the new folder in (Required)
        :param kwargs:
            color: The Folders color
            parent_folder_id: The ID of the folder you want to nest the new one under. Nesting is limited to 1 Tier.
        :return: UUID of the newly created folder.
        """

        folder_name = f"\"{name}\""
        arg_string = f'name: {folder_name}, workspace_id: {workspace_id}, '
        for key, value in kwargs.items():
            arg_string = arg_string + f"{key}: {value}, "
        arg_string = arg_string[:-2]
        query_string = f'''mutation {{create_folder ({arg_string}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['create_folder']['id']

    ####################################################################################################################
    def update_folder(self, folder_id, **kwargs):
        """
        Update a folder in a workspace. Pass keyword arguments to configure folder attributes. **Keywords must be passed
        exactly as defined below. Folder colors can be found here:
        https://asset.cloudinary.com/monday-platform-dev/3e39afb2309b512f4f53cc9173554d48
        :param folder_id: UUID of the folder to update. (Required)
        :param kwargs:
            name: Updated name of the folder
            color: Updated folder color
            parent_folder_id: The ID of the folder you want to nest the updated one under.
        :return: None
        """
        if 'name' in kwargs.keys():
            kwargs['name'] = f"\"{kwargs['name']}\""
        arg_string = f"folder_id: {folder_id}, "
        for key, value in kwargs.items():
            arg_string = arg_string + f"{key}: {value}, "
        arg_string = arg_string[:-2]
        query_string = f'''mutation {{update_folder ({arg_string}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    def delete_folder(self, folder_id):
        """
        Delete a folder from a workspace
        :param folder_id: UUID of the folder to delete
        :return: None
        """
        query_string = f'''mutation {{delete_folder (folder_id: {folder_id}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    # NOTIFICATIONS
    ####################################################################################################################
    def create_notification(self, user_id, target, body, target_type):
        """
        Send a notification to a user.
        :param user_id: UUID of the user to send the notification to.
        :param target: The target's unique identifier. The value depends on the target_type
        :param body: The notification's text.
        :param target_type: the target's type: project or post.
            - Project: sends a notification referring to a specific item or board
            - Post : sends a notification referring to a specific item's update or reply
        :return: None
        """
        query_string = f'''mutation {{create_notification 
        (user_id: {user_id}, target_id: {target}, text: "{body}", target_type: {target_type}) {{text}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    # UPDATES
    ####################################################################################################################
    def get_item_updates(self, item_id):
        """
        Get the updates from an item.
        :param item_id: UUID of the item.
        :return: Array of Dictionaries containing the update data. Return None on API call failure.
        """
        query_string = f'''{{items(ids:{item_id})
        {{updates {{id text_body, updated_at created_at creator_id 
        replies {{text_body created_at creator_id}} 
        assets {{id public_url}}}}}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['items'][0]['updates']

    ####################################################################################################################
    def create_update(self, item_id, update_text):
        """
        Create an update on an item.
        :param item_id: UUID of the item to leave the update on.
        :param update_text: Body of the update.
        :return: UUID of the update. Return None on API call failure.
        """
        query_string = f'''mutation {{create_update (item_id: {item_id}, body: "{update_text}") {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['create_update']['id']

    ####################################################################################################################
    def create_reply(self, item_id, update_text, parent_id):
        """
        Create an update on an item.
        :param item_id: UUID of the item to leave the update on.
        :param update_text: Body of the update.
        :param parent_id: UUID of the update to leave a reply on.
        :return: UUID of the Reply. Return None on API call failure.
        """
        query_string = f'''mutation {{
        create_update (item_id: {item_id}, body: "{update_text}", parent_id: {parent_id}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['create_update']['id']

    ####################################################################################################################
    def delete_update(self, update_id):
        """
        Delete an update on an item.
        :param update_id: UUID of the item.
        :return: None.
        """
        query_string = f'''mutation {{delete_update (id: {update_id}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    def clear_updates(self, item_id):
        """
        Clear all updates from an item.
        :param item_id: UUID of the item.
        :return: None.
        """
        query_string = f'''mutation {{clear_item_updates (item_id: {item_id}) {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    # FILES
    ####################################################################################################################
    def get_assets(self, item_id):
        """
        Get the assets(files) associated with an item.
        :param item_id: UUID of the item.
        :return: Array of dictionaries containing asset data. Return None on API call failure.
        """
        query_string = f'''{{items(ids:{item_id}){{assets {{id name file_size created_at public_url url}}}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['items'][0]['assets']

    ####################################################################################################################
    def upload_file_to_column(self, item_id, column_id, filepath):
        """
        Upload a local file to a file type column of an item. Remote files not supported.
        :param item_id: UUID of the item
        :param column_id: Column ID to upload the file to.
        :param filepath: Absolute Path to file on the local system. File Extension required.
        :return: UUID of the asset.
        """
        file_name = os.path.basename(filepath)
        payload = {
            'query': f'mutation add_file($file: File!) {{add_file_to_column (item_id: {item_id}, '
                     f'column_id: "{column_id}" file: $file) {{id}}}}', 'map': '{"column_file": "variables.file"}'}
        files = [('column_file', (f'{file_name}', open(filepath, 'rb'), 'application/octet-stream'))]

        response = self.__upload_file(payload, files)
        if not response:
            return None
        return response['data']['add_file_to_column']['id']

    ####################################################################################################################
    def add_file_to_update(self, update_id, file_path):
        """
        Upload a local file to an update. Remote files not supported.
        :param update_id: UUID of the update.
        :param file_path: Absolute Path to the local file. File Extension Required.
        :return:
        """
        file_name = os.path.basename(file_path)
        payload = {
            'query': f'mutation ($file: File!) {{add_file_to_update(file: $file, update_id: {update_id}) {{id}}}}',
            'map': '{"update_file":"variables.file"}'}
        files = [('update_file', (f'{file_name}', open(f'{file_path}', 'rb'), 'application/octet-stream'))]
        response = self.__upload_file(payload, files)
        if not response:
            return None
        return response['data']['add_file_to_update']['id']

    ####################################################################################################################
    # ITEMS
    ####################################################################################################################
    def __get_next_page(self, cursor, items, item_attributes):
        """
        Get the next set of 100 records using cursor based pagination. Max number of records which can be returned per
        API call is 100. Default is 25.
        :param cursor: Token based cursor used to retrieve the next set of records. Loop ends when this value is None.
        :param items: Initial items
        :param item_attributes: Item attributes to retrieve.
        :return: Array of Dictionaries containing item Data.
        """
        while cursor is not None:
            subsequent_query = f'''query 
            {{next_items_page (limit: 100, cursor: "{cursor}") {{cursor items {{{item_attributes}}}}}}}'''
            next_data = {'query': subsequent_query}
            next_response = self.__send_post_request(next_data)

            if not next_response:
                return None
            next_items = [item for item in next_response['data']['next_items_page']['items']]
            items = items + next_items
            cursor = next_response['data']['next_items_page']['cursor']

        return items

    ####################################################################################################################
    def get_item_ids_from_group(self, board_id, group_id):
        """
        Get all item IDs from a specific group on a board. Cursor Based Pagination Required. Records limited to 100
        per call.
        :param board_id: UUID of the board.
        :param group_id: UUID of the group.
        :return: Array of Item IDs
        """
        item_attributes = "id"
        initial_query = f'''query {{boards (ids: {board_id})
        {{groups(ids: "{group_id}") {{items_page (limit: 500) {{cursor items{{{item_attributes}}}}}}}}}}}'''
        data = {'query': initial_query}
        response = self.__send_post_request(data)

        if not response:
            return None
        item_ids = [item for item in response['data']['boards'][0]['groups'][0]['items_page']['items']]
        cursor = response['data']['boards'][0]['groups'][0]['items_page']['cursor']
        if cursor is None:
            item_ids = [item['id'] for item in item_ids]
            return item_ids
        all_item_ids = self.__get_next_page(cursor, item_ids, item_attributes)
        all_item_ids = [int(item['id']) for item in all_item_ids]
        return all_item_ids

    ####################################################################################################################
    def get_items_page_from_group(self, board_id, group_id, columns):
        column_string = ""
        for column in columns:
            column_string = column_string + f"\"{column}\", "
        column_string = column_string[:-2]
        column_string = f"[{column_string}]"
        item_attributes = f'''name id parent_item{{id name }} column_values(ids: {column_string}) {{text value
        column{{id title}}
        ... on BoardRelationValue {{display_value linked_items {{id}}}}
        ... on MirrorValue {{display_value}}}}'''

        initial_query = f'''{{boards(ids: {board_id}) {{groups(ids: "{group_id}") {{items_page(limit: 8) {{
        cursor
        items {{{item_attributes}}}}}}}}}}}'''
        data = {'query': initial_query}
        response = self.__send_post_request(data)
        if not response:
            return None
        items = [item for item in response['data']['boards'][0]['groups'][0]['items_page']['items']]
        cursor = response['data']['boards'][0]['groups'][0]['items_page']['cursor']
        if cursor is None:
            return items
        all_items = self.__get_next_page(cursor, items, item_attributes)
        return all_items

    ####################################################################################################################
    def get_items_with_status(self, board_id, group_id, columns, column_id, index_value):
        column_string = ""
        for column in columns:
            column_string = column_string + f"\"{column}\", "
        column_string = column_string[:-2]
        column_string = f"[{column_string}]"
        item_attributes = f'''name id parent_item{{id name }} column_values(ids: {column_string}) {{text value
        column{{id title}}
        ... on BoardRelationValue {{display_value linked_items {{id}}}}
        ... on MirrorValue {{display_value}}}}'''

        initial_query = f'''{{boards(ids: {board_id}) {{groups(ids: "{group_id}") {{items_page(limit: 100 
        query_params: {{rules: {{column_id: "{column_id}", compare_value: [{index_value}]}}}}) {{
        cursor
        items {{{item_attributes}}}}}}}}}}}'''
        data = {'query': initial_query}
        response = self.__send_post_request(data)
        if not response:
            return None
        items = [item for item in response['data']['boards'][0]['groups'][0]['items_page']['items']]
        cursor = response['data']['boards'][0]['groups'][0]['items_page']['cursor']
        if cursor is None:
            return items
        all_items = self.__get_next_page(cursor, items, item_attributes)
        return all_items

    ####################################################################################################################
    def get_item_ids_between_dates(self, board_id, group_id, column_id, start_date, end_date):
        """
        Get Item IDs between a specified date range. Supports Timeline columns and start dates.
        :param board_id: UUID of the board the items are on.
        :param group_id: UUID of the group the items are in.
        :param column_id: UUID of the timeline column to filter on.
        :param start_date: Start of date range.
        :param end_date: End of date range.
        :return: Array containing Item IDs
        """
        item_attributes = "id"
        initial_query = f'''{{boards(ids: {board_id}) {{groups(ids: "{group_id}") {{items_page(limit: 500
        query_params: {{rules: {{column_id: "{column_id}", compare_value: ["{start_date}", "{end_date}"], 
        compare_attribute: "START_DATE", operator: between}}}}) {{
        cursor items {{id}}}}}}}}}}'''
        data = {'query': initial_query}
        response = self.__send_post_request(data)
        if not response:
            return None
        item_ids = [item for item in response['data']['boards'][0]['groups'][0]['items_page']['items']]
        cursor = response['data']['boards'][0]['groups'][0]['items_page']['cursor']
        if cursor is None:
            item_ids = [item['id'] for item in item_ids]
            return item_ids
        all_item_ids = self.__get_next_page(cursor, item_ids, item_attributes)
        all_item_ids = [int(item['id']) for item in all_item_ids]
        return all_item_ids

    ####################################################################################################################
    def get_item_ids_between_date(self, board_id, group_id, column_id, start_date, end_date):
        """
        Get Item IDs between a specified date range. Supports Date columns.
        :param board_id: UUID of the board the items are on.
        :param group_id: UUID of the group the items are in.
        :param column_id: UUID of the date column to filter on.
        :param start_date: Start of date range.
        :param end_date: End of date range.
        :return: Array containing Item IDs
        """
        item_attributes = "id"
        initial_query = f'''{{boards(ids: {board_id}) {{groups(ids: "{group_id}") {{items_page(limit: 500
        query_params: {{rules: {{column_id: "{column_id}", compare_value: ["{start_date}", "{end_date}"], 
        operator: between}}}}) {{
        cursor items {{id}}}}}}}}}}'''
        data = {'query': initial_query}
        response = self.__send_post_request(data)
        if not response:
            return None
        item_ids = [item for item in response['data']['boards'][0]['groups'][0]['items_page']['items']]
        cursor = response['data']['boards'][0]['groups'][0]['items_page']['cursor']
        if cursor is None:
            item_ids = [item['id'] for item in item_ids]
            return item_ids
        all_item_ids = self.__get_next_page(cursor, item_ids, item_attributes)
        all_item_ids = [int(item['id']) for item in all_item_ids]
        return all_item_ids

    ####################################################################################################################
    def get_item_columns(self, item_list, column_id_list):
        """
        Get column values of items on a board.
        :param item_list: Array of item ids to query. Item IDs must be submitted as Integers.
        :param column_id_list: Array of column UUIDs. Column IDs must be submitted as strings.
        :return: Array of Dictionaries containing item and column values.
        """
        asyncio.run(self.__column_task_handler(item_list, column_id_list))
        global results
        current_results = results
        results = []
        return current_results[0]['data']['items']

    ####################################################################################################################
    def create_item(self, board, group, item_name):
        """
        Create a new item within a group on a specific board.
        :param board: UUID of the board to create the item on.
        :param group: UUID of the group to create the item in.
        :param item_name: Name of the new item to be created.
        :return: UUID of the newly created item. Return None on API call failure.
        """
        query_string = f'''mutation {{
        create_item (board_id: {board}, group_id: "{group}", item_name: "{item_name}") {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        return response['data']['create_item']['id']

    ####################################################################################################################
    def create_item_with_column_values(self, board, group, item_name, column_dict):
        """
        Create a New item within a group on a board. Populate specific column values on item creation.
        :param board: UUID of the board to create the item on.
        :param group: UUID of the group to create the item in.
        :param item_name: Name of the new item.
        :param column_dict: Dictionary of column values to set when item is created
        format: columns = {"column_id": {"type": "column_type", "values": ["value1", "value2", "etc"]}
        :return: UUID of the newly created item.
        """
        column_string = self.column_id_formatter(column_dict)
        query_string = f'''mutation {{
                create_item (board_id: {board}, group_id: "{group}", item_name: "{item_name}", 
                column_values: "{column_string}") {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)
        if not response:
            return None
        return response['data']['create_item']['id']

    ####################################################################################################################
    def delete_item(self, item_id):
        """
        Delete an item from the platform.
        :param item_id: UUID of the item to delete.
        :return: None.
        """
        query_string = f'''mutation {{delete_item (item_id: {item_id}) {{id}}}}'''
        data = {"query": query_string}
        response = self.__send_post_request(data)
        if not response:
            print("Error, Item could not be deleted")
        if response:
            print(f"Item {item_id} successfully deleted")

    ####################################################################################################################
    # COLUMNS
    ####################################################################################################################
    @staticmethod
    def column_id_formatter(column_dictionary):
        """
        Takes the column values dictionary and converts it into a correctly formatted GraphQL query string.
        :param column_dictionary: Dictionary containing column id, column type and required values for the query.
        :return: JSON formatted GraphQL query for column values.
        """
        global column_values
        query_string = "{"
        for (key, value) in column_dictionary.items():
            value_arguments = [key]
            for each_value in value['values']:
                value_arguments.append(each_value)
            column_string = column_values[value['type']].format(*value_arguments)
            query_string = query_string + f"{column_string}, "
        query_string = query_string[:-2]
        query_string = query_string + "}"
        return query_string

    ####################################################################################################################
    def change_column_values(self, board_id, item_id, column_dict):
        """
        Change the column values of an item. Multiple column values can be changed in a single query.
        :param board_id: UUID of the board the item is on.
        :param item_id: UUID of the Item the column values should be changed on.
        :param column_dict: Dictionary containing column IDs, column types and values.
        :return: None.
        """
        column_string = self.column_id_formatter(column_dict)
        query_string = f'''mutation {{change_multiple_column_values (item_id: {item_id}, board_id: {board_id}, 
        column_values: "{column_string}") {{id}}}}'''
        data = {'query': query_string}
        response = self.__send_post_request(data)
        print(response)

    ####################################################################################################################
    # SUBITEMS
    ####################################################################################################################
    def get_subitems(self, item_id):
        """
        Get the UUIDs of the subitems of an item
        :param item_id: UUID of the parent Item
        :return: Array of subitem IDs. Return None on API call failure.
        """
        query_string = f'''{{items (ids: {item_id}) {{subitems {{id}}}}}}'''
        data = {"query": query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        subitem_ids = [item['id'] for item in response['data']['items'][0]['subitems']]
        return subitem_ids

    ####################################################################################################################
    def get_subitem_info(self, sub_item_id):
        """
        Get the Board ID and Parent ID from a Subitem.
        :param sub_item_id: UUID of the subitem.
        :return: Dictionary containing the parent ID and Board ID of the subitem.
        """
        query_string = f'''{{items(ids: {sub_item_id}) {{parent_item {{id}} board {{id}}}}}}'''
        data = {"query": query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        parent_item = response['data']['items'][0]['parent_item']['id']
        board = response['data']['items'][0]['board']['id']
        subitem_dictionary = {"Parent Item": parent_item, "Subitem Board": board}
        return subitem_dictionary

    ####################################################################################################################
    def create_subitem(self, parent_id, item_name, column_dictionary):
        """
        Create a new Subitem under a Parent Item.
        :param parent_id: UUID of the item to create the subitem under.
        :param item_name: Name of the new Subitem.
        :param column_dictionary: Dictionary containing column IDs, column types and values.
        :return: Dictionary containing the newly created Subitem ID and the board ID on which the subitem was created.
        """
        column_string = self.column_id_formatter(column_dictionary)
        query_string = f'''mutation {{create_subitem (parent_item_id: {parent_id}, item_name: "{item_name}", 
        column_values: "{column_string}") {{id board {{id}}}}}}'''
        data = {"query": query_string}
        response = self.__send_post_request(data)
        if not response:
            return None
        board_id = response['data']['create_subitem']['board']['id']
        new_item_id = response['data']['create_subitem']['id']
        new_item_dict = {"Item ID": new_item_id, "Subitem Board": board_id}
        return new_item_dict

    ####################################################################################################################
    # END
    ####################################################################################################################
