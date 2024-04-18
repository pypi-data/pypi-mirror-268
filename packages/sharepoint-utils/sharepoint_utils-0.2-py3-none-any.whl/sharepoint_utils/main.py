#########################################################################################

# Import necessary modules for authentication and working with SharePoint files
from office365.sharepoint.files.creation_information import FileCreationInformation
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from io import StringIO
import pandas as pd
import io

#########################################################################################

def connect_to_sharepoint(username, password, site_address):
    """
    This function connects to a SharePoint site using the provided username, password, and site address.
    
    :param username: The username to authenticate with SharePoint.
    :param password: The password to authenticate with SharePoint.
    :param site_address: The address of the SharePoint site.
    :return: ClientContext object if successful, None otherwise.
    """
    
    # Define SharePoint base URL
    sharepoint_base_url = site_address

    # Specify SharePoint user credentials
    sharepoint_user = username
    sharepoint_password = password

    # Authenticate with SharePoint
    ctx_auth = AuthenticationContext(sharepoint_base_url)
    if ctx_auth.acquire_token_for_user(sharepoint_user, sharepoint_password):
        ctx = ClientContext(sharepoint_base_url, ctx_auth)
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()

        # Print a message indicating successful connection to SharePoint along with the web title
        print('Connected to SharePoint: ', web.properties['Title'])
        return ctx
    else:
        print("Failed to authenticate with SharePoint.")
        return None

#########################################################################################

def combine_files_into_dataframe(ctx, folder_url):
    """
    Combine files from a SharePoint folder into a single pandas DataFrame.
    
    :param ctx: ClientContext object authenticated with SharePoint.
    :param folder_url: Server-relative URL of the SharePoint folder containing files.
    :return: Combined pandas DataFrame if successful, None otherwise.
    """
    try:
        # Get the folder object using the provided folder URL
        folder = ctx.web.get_folder_by_server_relative_url(folder_url)

        # Get the collection of files in the folder
        files = folder.files

        # Load the files collection
        ctx.load(files)

        # Execute the query to retrieve the files
        ctx.execute_query()

        # Initialize an empty list to store individual DataFrames
        all_data_frames = []

        # Iterate through each file in the folder
        for file in files:
            # Get the name of the file
            file_name = file.properties["Name"]

            # Open the file and get its content
            response = File.open_binary(ctx, file.serverRelativeUrl)
            file_content = response.content

            # Check the file extension to determine the file type
            if file_name.lower().endswith('.csv'):
                # Read CSV file content into a pandas DataFrame using BytesIO
                df = pd.read_csv(io.BytesIO(file_content))
            elif file_name.lower().endswith('.xlsx'):
                # Read XLSX file content into a pandas DataFrame
                df = pd.read_excel(io.BytesIO(file_content))
            else:
                # Skip files with unsupported extensions
                continue

            # Append the DataFrame to the list
            all_data_frames.append(df)

        # Concatenate all individual DataFrames into a single DataFrame
        combined_df = pd.concat(all_data_frames, ignore_index=True)

        # Return the combined DataFrame
        return combined_df

    # Handle any exceptions that may occur during file reading
    except Exception as e:
        print('Problem reading files: ', e)
        return None

#########################################################################################

def upload_dataframe_to_sharepoint(ctx, folder_path, dataframe, file_name):
    """
    This function uploads a pandas DataFrame to a SharePoint folder as a CSV file.

    Parameters:
    ctx (ClientContext): The SharePoint ClientContext.
    folder_path (str): The server-relative URL of the SharePoint folder where the file will be uploaded.
    dataframe (DataFrame): The pandas DataFrame to be uploaded.
    file_name (str): The name of the file to be created.
    """

    try:
        # Get the SharePoint folder
        folder = ctx.web.get_folder_by_server_relative_url(folder_path).select(["Exists"]).get().execute_query()
        
        # Convert the DataFrame to a CSV string
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer, index=False)
        file_content = csv_buffer.getvalue().encode('utf-8-sig')

        # Upload the file to the folder
        file = folder.upload_file(file_name, file_content).execute_query()
        print(f"File has been uploaded into: {file.serverRelativeUrl}")
    
    except Exception as e:
        print(f"An error occurred while uploading the file: {str(e)}")

#########################################################################################
