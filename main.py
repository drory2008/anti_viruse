import scan_report
import files_path
dirctory_path= r"C:\Users\matan\py-job"
ls=files_path.process_files_in_directory(dirctory_path)
scan_report.main(ls)