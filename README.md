# DJ-Comps-Book-Exchange
Book Exchange Web-app for exchange and transfer of books between juniors and seniors.

----------

## Features:

- Forum to post a request for books: The forum can be used to ask for specific books, links to books, advice about ideal books to use etc. The forum has topics, posts and threads (like StackOverflow).
- One to one chat for potential buyers/borrowers and sellers/lenders: The chat connects potential  buyers with the seller, to discuss prices, books to exchange, time of meeting etc.
- Tags associated with books for efficient searching of books. Semester-wise and topic-wise segregation of books. 
- Inventory containing books along with the status (available/unavailable) posted by various lenders. Details of the book and the lender can be obtained by clicking on the book. Users can flag incorrect listings to notify the lender and other users as well.
- Actual exchange of book will happen offline once the buyer/borrower has contacted the seller/lender using the details present on the website. 
- User Dashboard: Every user has a dashboard to add listings, view their listings and the books borrowed. There are tabs on the dashboard displaying lended books, borrowed books and a way for sellers/lenders to add new listings to the website. Only the seller/lender of a particular  book has  the right to change the listings for the same.  
- Special tabs: Tab containing books categorized according to semester, recently added etc.  

----------

### Instructions to setup postgres

 1. sudo apt-get update
 2. sudo apt-get install postgresql
 3. sudo su - postgres
 4. psql
 5. CREATE DATABASE booke;
 6. CREATE USER johndory WITH PASSWORD 'abc@123';
 7. ALTER ROLE johndory SET client_encoding TO 'utf8';
 8. ALTER ROLE johndory SET default_transaction_isolation TO 'read committed';
 9. ALTER ROLE johndory SET timezone TO 'UTC';
 10. GRANT ALL PRIVILEGES ON DATABASE booke TO johndory;
 11. \q
 12. exit

----------
- pip3 install -r requirements.txt
