import cx_Oracle
from datetime import datetime, timedelta, date

conn=cx_Oracle.connect('LMS/LMS@localhost:1521/XEPDB1')
cur=conn.cursor()

#                           -----------LOGIN AND SIGNUP FUNCTION-----------
current_admin_id = None  # Declare global variable

def login(admin_id: int, password: str) -> bool:
    '''
    Verifies the admin's login credentials.

    Parameters:
    - admin_id (int): The admin ID.
    - password (str): The admin password.

    Returns:
    bool: True if the login is successful, False otherwise.
    '''

    global current_admin_id

    try:
        # Check if the admin ID and password exist in the authentication table
        cur.execute("SELECT COUNT(*) FROM authentication_system WHERE admin_id = :1 AND password = :2",
                    (admin_id, password))
        count = cur.fetchone()[0]

        if count == 1:
            current_admin_id = admin_id  # Store admin ID in global variable
            # print("Login successful.")
            return True
        else:
            # print("Invalid admin ID or password.")
            return False

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)
        return False

# ------------------------------------------ ADD ADMIN FUNCTION -----------------------------
admin_id = None

def add_admin(password: str, staff_id: int) -> None:
    '''
    Adds a new admin if the staff is present in the staff table and is not already an admin.
    Updates the login table with the admin ID and staff ID.

    Parameters:
    - password (str): The admin password.
    - staff_id (int): The staff ID.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while adding the admin or updating the login table.
    '''

    global admin_id  # Declare the global variable

    try:
        # Check if the staff ID exists in the staff table
        cur.execute("SELECT COUNT(*) FROM staff WHERE staff_id = :1", (staff_id,))
        count = cur.fetchone()[0]

        if count == 0:
            # print("Invalid staff ID.")
            return "Invalid staff ID."

        # Check if the staff is already an admin
        cur.execute("SELECT COUNT(*) FROM login WHERE staff_id = :1", (staff_id,))
        count = cur.fetchone()[0]

        if count > 0:
            # print("This staff is already an admin.")
            return "This staff is already an admin."

        # Generate the new admin ID
        cur.execute("SELECT COALESCE(MAX(admin_id), 0) + 1 FROM authentication_system")
        admin_id = cur.fetchone()[0]
        
        # Assign the admin ID to the global variable
        admin_id = admin_id

        # Insert a new admin into the authentication table
        cur.execute("INSERT INTO authentication_system (admin_id, password) VALUES (:1, :2)", (admin_id, password))

        # Update the login table with the admin ID and staff ID
        cur.execute("INSERT INTO login (admin_id, staff_id) VALUES (:1, :2)", (admin_id, staff_id))

        conn.commit()
        # print("Admin added successfully.")
        return "Admin added successfully."

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)

def generateAdminID():
    # Generate the new admin ID
    cur.execute("SELECT COALESCE(MAX(admin_id), 0) + 1 FROM authentication_system")
    admin_id = cur.fetchone()[0]

    return admin_id


#--------------------------------------------MEMBERS FUUNCTION------------------------------

#-------------------------------------------INSERT MEMBER FUNCTION--------------------------
def insert_member(f_name:str, l_name:str, email:str, contact_no:int, address:str) -> None:
    '''
    This function inserts a member into the member table.

    Parameters:
    - f_name (str): The first name of the member.
    - l_name (str): The last name of the member.
    - email (str): The email address of the member.
    - contact_no (int): The contact number of the member.
    - address (str): The residential address of the member.

    Returns:
    None
    '''

    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to insert a member
        if designation.lower() != 'member manager':
            # print("You don't have the authority to insert a member.")
            return "You don't have the authority to insert a member."

        last_member_id = cur.execute('''SELECT member_id FROM members WHERE member_id =
                                        (SELECT MAX(member_id) FROM members)''')
        member_id = last_member_id.fetchone()[0] + 1

        insert_mem = '''
            INSERT INTO members (MEMBER_ID, FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, CONTACT_NUMBER, RESIDENTIAL_ADDRESS)
            VALUES (:1, :2, :3, :4, :5, :6)
        '''
        cur.execute(insert_mem, (member_id, f_name, l_name, email, contact_no, address))
        conn.commit()
        return "Member Inserted Successfully"

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Error occurred while inserting member:", error.message)

    except Exception as e:
        print("An error occurred:", str(e))

#                           --------UPDATE MEMBER FUNCTION-----------

def update_member(member_id: int, address: str, contact_number: int, email: str) -> None:
    '''
    This function updates the details of a member in the member table.

    Parameters:
    - member_id (int): The ID of the member to be updated.
    - address (str): The new residential address of the member.
    - contact_number (int): The new contact number of the member.
    - email (str): The new email address of the member.

    Raises:
    - Exception: If an error occurs while updating the member or if the current admin is not authorized.

    Returns:
    None
    '''

    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to update a member
        if designation.lower() != 'member manager':
            # print("You don't have the authority to update a member.")
            return "You don't have the authority to update a member."

        sql = "UPDATE members SET residential_address = :1, contact_number = :2, email_address = :3 WHERE member_id = :4"
        cur.execute(sql, (address, contact_number, email, member_id))
        conn.commit()
        return "Member updated successfully!"

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        error_message = "Error occurred while updating member: " + error.message
        raise Exception(error_message)

    except Exception as e:
        error_message = "An error occurred: " + str(e)
        raise Exception(error_message)

#                    ----------VIEW ALL MEMBER FUNCTION -----------

def view_all_members() -> tuple:
    '''
    Retrieves all members from the member table.

    Returns:
    tuple: A tuple containing all members retrieved from the member table.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while retrieving members.
    '''

    try:
        view_mem = '''SELECT * FROM MEMBERS ORDER BY member_id'''
        all_mem = cur.execute(view_mem)
        result = all_mem.fetchall()
        # for member in result:
        #     print(member)

        return result

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)
        return ()

#                    ------------DELETE MEMBER FUNCTION--------------
def delete_member(member_id: int) -> None:
    '''
    Deletes a member from the member table.

    Parameters:
    - member_id (int): The ID of the member to be deleted.

    Returns:
    None

    Raises:
    - ValueError: If the member has borrowed books or if the current admin is not authorized.
    - cx_Oracle.DatabaseError: If an error occurs while deleting the member.
    '''

    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to delete a member
        if designation.lower() != 'member manager':
            return "You don't have the authority to delete a member."
            raise ValueError("You don't have the authority to delete a member.")

        # Check if the member has any borrowed books
        cur.execute("SELECT COUNT(*) FROM borrow WHERE member_id = :1", (member_id,))
        count = cur.fetchone()[0]

        if count > 0:
            return "Cannot delete member. They have borrowed books."
            raise ValueError("Cannot delete member. They have borrowed books.")

        # Delete the member from the member table
        cur.execute("DELETE FROM members WHERE member_id = :1", (member_id,))
        conn.commit()
        return "Member deleted successfully!"
        print("Member deleted successfully!")

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)

    except ValueError as e:
        print("Error:", str(e))

    # finally:
    #     cur.close()
    #     conn.close()

#                   ------------------SEARCH MEMBER FUNCTION--------------------------
def search_member(search_term) -> tuple:
    '''
    Searches for members in the member table based on the search term.

    Parameters:
    - search_term (str): The search term to match against member ID or first name.

    Returns:
    tuple: A tuple containing the search results.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while searching for members.
    '''

    try:
        search_mem = "SELECT * FROM members WHERE first_name LIKE :term OR member_id LIKE :term"
        search_mem = cur.execute(search_mem, term=search_term)
        result = search_mem.fetchall()
        if result:
            return result[0]
            print(result)
        else:
            return None
            print('No Member found')

        return 

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)
        return ()

#------------------------------------SEARCH BORROWED BOOK FUNCTON-----------------------------------------
def search_borrowed_books(member_id:int)->tuple:
    '''
    Searches for books borrowed by a specific member.

    Parameters:
    - member_id (int): The ID of the member.

    Returns:
    list: A list of tuples representing the borrowed books, each tuple containing the book details.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while searching for borrowed books.
    '''

    try:
        sql = '''
            SELECT b.BOOK_ID, b.BOOK_TITLE, m.FIRST_NAME, m.LAST_NAME
            FROM books b
            JOIN borrow br ON b.BOOK_ID = br.BOOK_ID
            JOIN members m ON m.MEMBER_ID = br.MEMBER_ID
            WHERE m.MEMBER_ID = :member_id
        '''
        cur.execute(sql, member_id=member_id)
        result = cur.fetchall()
        
        if result:
            for book in result:
                print("Book ID:", book[0])
                print("Title:", book[1])
                print("Borrowed by:", book[2], book[3])
                print()
        else:
            print("No borrowed books found for the member.")

        return result

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)
        return []
    
#-------------------------------------Member request to borrow book--------------------------------------

def borrow_book(member_id: int, book_id: int , book_fee: int) -> None:
    '''
    Borrow a book by a member and update the no_of_copies attribute in the books table.

    Parameters:
    - member_id (int): The ID of the member borrowing the book.
    - book_id (int): The ID of the book being borrowed.
    - book_fee (int): The fee associated with borrowing the book.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while borrowing the book.
    '''

    try:
        # Check if the book is available (number_of_copies > 0)
        cur.execute("SELECT number_of_copies FROM books WHERE book_id = :1", (book_id,))
        no_of_copies = cur.fetchone()[0]

        if no_of_copies == 0:
            return "Book is not available for borrowing."
            print("Book is not available for borrowing.")

        # Get the current date as the issue date
        issue_date = datetime.now().strftime("%d-%b-%Y")

        # Calculate the due date as 7 days after the issue date
        issue_date_obj = datetime.strptime(issue_date, "%d-%b-%Y")
        due_date_obj = issue_date_obj + timedelta(days=7)
        due_date = due_date_obj.strftime("%d-%B-%Y")

        # Insert a new row into the borrow table
        cur.execute('''INSERT INTO borrow (member_id, book_id, book_fee, issue_date, due_date)
                     VALUES (:1, :2, :3, TO_DATE(:4, 'dd-mon-yyyy'), TO_DATE(:5, 'dd-mon-yyyy'))''',
                    (member_id, book_id, book_fee, issue_date, due_date))

        # Update the no_of_copies in the books table
        cur.execute("UPDATE books SET number_of_copies = number_of_copies - 1 WHERE book_id = :1", (book_id,))

        conn.commit()
        return "Book issued successfully."
        print("Book borrowed successfully.")

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)



#--------------------------------------Return borrow book-----------------------------------------------


def return_borrow_book(member_id: int, book_id: int) -> None:
    '''
    Return a borrowed book by a member and update the return date in the borrow table.

    Parameters:
    - member_id (int): The ID of the member returning the book.
    - book_id (int): The ID of the book being returned.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while returning the book.
    '''

    try:
        # Check if the member and book exist in the borrow table
        cur.execute("SELECT COUNT(*) FROM borrow WHERE member_id = :1 AND book_id = :2",
                    (member_id, book_id))
        count = cur.fetchone()[0]

        if count == 0:
            print("This member did not borrow the specified book.")
            return

        # Update the return date in the borrow table for the specific member and book
        today = date.today()
        today = today.strftime("%d-%B-%Y")
        cur.execute('''UPDATE borrow SET return_date = :1 WHERE member_id = :2 AND book_id = :3''',
                    (today, member_id, book_id))

        conn.commit()
        return "Book returned successfully."
        print("Book returned successfully.")

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)

#--------------------------------------view borrow books-----------------------------------
def borrow_book_current(member_id: int) -> None:
    '''
    Retrieves the book currently borrowed for a specific member ID from the borrow table.

    Parameters:
    - member_id (int): The ID of the member.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while retrieving the book borrowing history.
    '''

    try:
        # Retrieve the book borrowing history for the specified member ID with a return date
        cur.execute("SELECT * FROM borrow WHERE member_id = :1 AND return_date IS NULL", (member_id,))
        history = cur.fetchall()

        if history:
            # print(f"Borrow Book History for Member ID {member_id}:")
            compHist = []
            for row in history:
                cur.execute("SELECT * FROM books WHERE book_id = :1", (row[0],))
                book_info = cur.fetchall()
                book_id = row[0]
                book_name = book_info[0][1]
                issue_date = row[3].date().strftime("%d-%B-%Y")
                due_date = row[4].date().strftime("%d-%B-%Y")
                # return_date = row[5].date().strftime("%d-%B-%Y")
                entry = (book_id, book_name, issue_date, due_date)
                compHist.append(entry)
                # print(f"Book ID: {book_id}, Book name: {book_name}, Issue Date: {issue_date}, Due Date: {due_date}, Return Date: {return_date}")
            return compHist
        else:
            return None
            print(f"No book borrowing history found for Member ID {member_id}.")

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)

#--------------------------------------view borrow history-----------------------------------
def borrow_book_history(member_id: int) -> None:
    '''
    Retrieves the book borrowing history for a specific member ID from the borrow table.

    Parameters:
    - member_id (int): The ID of the member.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while retrieving the book borrowing history.
    '''

    try:
        # Retrieve the book borrowing history for the specified member ID with a return date
        cur.execute("SELECT * FROM borrow WHERE member_id = :1 AND return_date IS NOT NULL", (member_id,))
        history = cur.fetchall()

        if history:
            # print(f"Borrow Book History for Member ID {member_id}:")
            compHist = []
            for row in history:
                cur.execute("SELECT * FROM books WHERE book_id = :1", (row[0],))
                book_info = cur.fetchall()
                book_id = row[0]
                book_name = book_info[0][1]
                issue_date = row[3].date().strftime("%d-%B-%Y")
                due_date = row[4].date().strftime("%d-%B-%Y")
                return_date = row[5].date().strftime("%d-%B-%Y")
                entry = (book_id, book_name, issue_date, due_date, return_date)
                compHist.append(entry)
                # print(f"Book ID: {book_id}, Book name: {book_name}, Issue Date: {issue_date}, Due Date: {due_date}, Return Date: {return_date}")
            return compHist
        else:
            return None
            print(f"No book borrowing history found for Member ID {member_id}.")

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)

#---------------------------------------View all book----------------------------------------
def view_all_book() -> tuple:
    '''
    Retrieves all members from the member table.

    Returns:
    tuple: A tuple containing all members retrieved from the member table.

    Raises:
    cx_Oracle.DatabaseError: If an error occurs while retrieving members.
    '''

    try:
        view_mem = '''SELECT * FROM BOOKS ORDER BY book_id'''
        all_mem = cur.execute(view_mem)
        result = all_mem.fetchall()
        # for book in result:
        #     print(book)

        return result

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("An error occurred:", error.message)
        return ()

#----------------------------------------------BOOKS----------------------------------------------------------

#-----------------------------------------insert book-----------------------------------------------------
def insert_book(book_id: int, book_title: str, author_name: str, publisher: str, number_of_copies: int, shelf_location: str) -> None:
    '''
    Insert a book into the books table.

    Args:
        book_id (int): The ID of the book.
        book_title (str): The title of the book.
        author_name (str): The name of the author.
        publisher (str): The publisher of the book.
        number_of_copies (int): The number of copies available.
        shelf_location (str): The shelf location of the book.

    Raises:
        ValueError: If any of the arguments are not provided or if the current admin is not authorized.
        Exception: Any other exception that may occur during the insertion process.
    '''

    if any(value is None for value in (book_id, book_title, author_name, publisher, number_of_copies, shelf_location)):
        raise ValueError("All arguments must be provided.")

    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to insert a book
        if designation.lower() != 'book manager':
            return "You don't have the authority to insert a book."
            raise ValueError("You don't have the authority to insert a book.")

        insert_book_query = '''
            INSERT INTO books (book_id, book_title, author_name, publisher, number_of_copies, shelf_location)
            VALUES (:1, :2, :3, :4, :5, :6)
        '''

        cur.execute(insert_book_query, (book_id, book_title, author_name, publisher, number_of_copies, shelf_location))
        conn.commit()

        return "Book inserted successfully."
        print("Book inserted successfully.")
    except cx_Oracle.DatabaseError as e:
        conn.rollback()
        print("Failed to insert book.")
        raise e
    except ValueError as e:
        print("Error:", str(e))
    # finally:
    #     cur.close()
    #     conn.close()

#----------------------------------------------update book---------------------------------------------
def update_book(book_id: int, new_copies: int, new_location: str) -> None:
    """
    Update the details of a book in the database.

    Args:
        book_id (int): The ID of the book to update.
        new_copies (int): The new number of copies of the book.
        new_location (str): The new shelf location of the book.

    Raises:
        ValueError: If the current admin is not authorized to update books.
        Exception: Any other exception that may occur during the update process.
    """
    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to update books
        if designation.lower() != 'book manager':
            return "You don't have the authority to update books."
            raise ValueError("You don't have the authority to update books.")

        update_query = """
            UPDATE books
            SET number_of_copies = :new_copies,
                shelf_location = :new_location
            WHERE book_id = :book_id
        """

        # Execute the update query with the provided parameters
        cur.execute(update_query, {
            'new_copies': new_copies,
            'new_location': new_location,
            'book_id': book_id
        })
        conn.commit()
        return "Book updated successfully"
        print("Book updated successfully")
    except cx_Oracle.DatabaseError as e:
        print("Error updating book:", str(e))
    except ValueError as e:
        print("Error:", str(e))
    # finally:
    #     cur.close()
    #     conn.close()
#------------------------------------------delete book-----------------------------------------
def delete_book(book_id: int) -> None:
    """
    Deletes a book from the database.

    Args:
        book_id (int): The ID of the book to be deleted.

    Raises:
        ValueError: If the current admin is not authorized to delete books or if the book is borrowed.
        Exception: Any other exception that may occur during the deletion process.
    """
    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to delete books
        if designation.lower() != 'book manager':
            return "You don't have the authority to delete books."
            raise ValueError("You don't have the authority to delete books.")

        # Check if the book exists in the books table
        cur.execute("SELECT COUNT(*) FROM books WHERE book_id = :1", (book_id,))
        count = cur.fetchone()[0]

        if count == 0:
            return "Book not found."
            print("Book not found.")
            return

        # Check if the book is borrowed
        cur.execute("SELECT COUNT(*) FROM borrow WHERE book_id = :1", (book_id,))
        borrow_count = cur.fetchone()[0]

        if borrow_count > 0:
            return "Cannot delete the book. It is currently borrowed."
            raise ValueError("Cannot delete the book. It is currently borrowed.")

        # Delete the book from the books table
        cur.execute("DELETE FROM books WHERE book_id = :1", (book_id,))
        conn.commit()
        return "Book deleted successfully."
        print("Book deleted successfully.")
    except cx_Oracle.DatabaseError as e:
        print("Error deleting book:", str(e))
    except ValueError as e:
        print("Error:", str(e))
    # finally:
    #     cur.close()
    #     conn.close()

#------------------------------------------search book-----------------------------------------

def search_books(search_term) -> tuple:
    """
    Search for books in the database based on the book ID OR title.

    Args:
        bookid (str): The book ID to search for.
        booktitle (str): The book title to search for.

    Returns:
        tuple: A tuple containing the search results as rows from the database.
    """
    try:
        search_mem = "SELECT * FROM books WHERE book_id LIKE :term OR book_title LIKE :term"
        search_mem = cur.execute(search_mem, term=search_term)
        result = search_mem.fetchall()
        if result:
            return result[0]
            print(result)
        else:
            None
            print('No book found')

        return
    except Exception as e:
        print("Error searching for books:", str(e))
        return ()

#------------------------------------STAFF FUNCTIONS------------------------------------------------------
def generateStaffID():
    last_staff_id = cur.execute('''SELECT staff_id FROM staff WHERE staff_id =
                     (SELECT MAX(staff_id) FROM staff)''')
    staff_id = last_staff_id.fetchone()[0] + 1
    return staff_id

def insert_staff(staff_name:str, designation:str)->None:
    '''
    Insert staff members into the staff table.

    Args:
        staff_name (str): The name of the staff member.
        designation (str): The designation of the staff member.
    '''
    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to update books
        if designation.lower() != 'Administrator':
            return "You don't have the authority to add staff details."
            raise ValueError("You don't have the authority to add staff details.")

        last_staff_id=cur.execute('''SELECT staff_id FROM staff WHERE staff_id =
                         (SELECT MAX(staff_id) FROM staff)''')
        staff_id=last_staff_id.fetchone()[0]+1

        insert_st = '''INSERT INTO staff (staff_id, staff_name, designation) VALUES (:1, :2, :3)'''
        cur.execute(insert_st, (staff_id, staff_name, designation))
        conn.commit()
        print("Staff inserted successfully")
    except Exception as e:
        print("Error inserting staff:", str(e))


# ----------------------------------------------update staff---------------------------------------------
def update_staff(staff_id: int, new_designation: str) -> None:
    """
    Update the details of a staff in the database.

    Args:
        staff_id (int): The ID of the staff to update.
        new_designation (str): The new designation of staff member.

    Raises:
        ValueError: If the current admin is not authorized to update staff.
        Exception: Any other exception that may occur during the update process.
    """
    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to update books
        if designation.lower() != 'Administrator':
            return "You don't have the authority to update staff details."
            raise ValueError("You don't have the authority to update staff details.")

        update_query = """
            UPDATE staff
            SET designation = :new_designation
            WHERE staff_id = :staff_id
        """

        # Execute the update query with the provided parameters
        cur.execute(update_query, {
            'new_designation': new_designation,
            'staff_id': staff_id
        })
        conn.commit()
        return "staff details updated successfully"
        print("staff details updated successfully")
    except cx_Oracle.DatabaseError as e:
        print("Error updating staff:", str(e))
    except ValueError as e:
        print("Error:", str(e))
    # finally:
    #     cur.close()
    #     conn.close()


# ------------------------------------------delete staff-----------------------------------------
def delete_staff(staff_id: int) -> None:
    """
    Deletes a staff from the database.

    Args:
        staff_id (int): The ID of the staff to be deleted.

    Raises:
        ValueError: If the current admin is not authorized to delete staff.
        Exception: Any other exception that may occur during the deletion process.
    """
    try:
        global current_admin_id

        # Check the designation of the current admin
        cur.execute("SELECT designation FROM staff WHERE staff_id IN (SELECT staff_id FROM login WHERE admin_id = :1)",
                    (current_admin_id,))
        designation = cur.fetchone()[0]

        # Check if the current admin has the authority to delete staff member.
        if designation.lower() != 'Administrator':
            return "You don't have the authority to delete staff details."
            raise ValueError("You don't have the authority to delete staff details.")

        # Check if the staff exists in the books table
        cur.execute("SELECT COUNT(*) FROM books WHERE book_id = :1", (staff_id,))
        count = cur.fetchone()[0]

        if count == 0:
            return "Staff not found."
            print("Staff not found.")

        # Delete the staff from the staff table
        cur.execute("DELETE FROM login WHERE staff_id = :1", (staff_id,))
        cur.execute("DELETE FROM manage WHERE staff_id = :1", (staff_id,))
        cur.execute("DELETE FROM staff WHERE staff_id = :1", (staff_id,))
        conn.commit()
        return "staff deleted successfully."
        print("staff deleted successfully.")

    except cx_Oracle.DatabaseError as e:
        print("Error deleting staff:", str(e))
    except ValueError as e:
        print("Error:", str(e))


def search_staff(search_term):
    '''This function searches for staff members in the staff table based on staff_id or staff_name.

    Args:
        staff_id (int): The ID of the staff member. OR
        staff_name (str): The name of the staff member.

    Raises:
        cx_Oracle.Error: If an error occurs during database connection or execution.

    '''       
    try:
        search_mem = "SELECT * FROM staff WHERE staff_name LIKE :term OR staff_id LIKE :term"
        search_mem = cur.execute(search_mem, term=search_term)
        result = search_mem.fetchall()
        if result:
            return result[0]
            print(result)
        else:
            return None
            print('No staff found')

        return

    except cx_Oracle.Error as error:
        print("Error occurred during staff search:", error)

if __name__=='__main__':
   pass

