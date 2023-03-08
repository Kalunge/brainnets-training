''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''


def transfer_files():
    """Transfer files from external FTP server to internal network."""
    # Connect to the FTP server and login.
    ftp = ftplib.FTP('ftp.example.com')
    ftp.login(user='user', passwd='password')

    # Change to the correct directory and get a list of the files.
    ftp.cwd('/files')
    files = ftp.nlst()

    # Create a local directory to store the files.
    if not os.path.exists('files'):
        os.makedirs('files')

    # Download each file from the FTP server and save it to the local directory.
    for file in files:
        with open(os.path.join('files', file), 'wb') as f:
            ftp.retrbinary('RETR ' + file, f.write)

    # Disconnect from the FTP server.
    ftp.quit()

    # Move the files from the local directory to the internal network.
    for file in files:
        shutil.move(os.path.join('files', file), '/internal/files')

    # Log the successful transfer.
    with open('transfer_log.txt', 'a') as f:
        f.write('Files transferred successfully at {}.\n'.format(datetime.now()))

    # Schedule the script to run daily at 5:00 AM.
    schedule.every().day.at('05:00').do(transfer_files)

    # Run the script until you close the terminal.
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    transfer_files()


