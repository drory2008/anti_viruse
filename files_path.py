import os

def process_files_in_directory(directory_path):
    paths=[]
    try:
        files = os.listdir(directory_path)
        
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)

            if os.path.isfile(file_path):
                paths.append(file_path)
            else:
                files_tat =os.listdir(file_path)
                for file_tat in files_tat:
                    file_path = os.path.join(file_path, file_tat)
        return paths       
    except FileNotFoundError:
        print(f"התיקייה {directory_path} לא נמצאה")
    except PermissionError:
        print(f"אין הרשאות לגישה לתיקייה {directory_path}")