# Football Ticketing System - Stadium Seat Management

This Python script, Football Ticketing System, simulates a seat and ticket management system for the **Şükrü Saraçoğlu Stadium**. It allows creating categories of seats, selling and canceling tickets, checking revenues, and displaying the seating layout. Made it for the assignment of BBM103 course, Introduction to Programming Laboratory.

## Features

### Category Management:

- Create seating categories with a specified number of rows and columns.  
- Each seat is initially free and uniquely identified by row (A–Z) and column numbers (0, 1, 2, ...).  

### Ticket Sales:

- Sell tickets for individual seats or seat ranges.  
- Supported ticket types:
  - Student: $10  
  - Full: $20  
  - Season: $250  
- Prevents selling already sold seats or invalid seat ranges.  

### Ticket Cancellation:

- Cancel tickets for previously sold seats.  
- Returns seats back to "free" status.  
- Warns if the seat is already free or outside valid range.  

### Balance Reports:

- Generate revenue reports for a category.  
- Shows the number of student, full, and season tickets sold, along with total revenue.  

### Seat Layout Visualization:

- Display the seating layout of a category.  
- Markings:
  - `X` = Free  
  - `S` = Student ticket  
  - `F` = Full ticket  
  - `T` = Season ticket  

## Usage

To utilize the Football Ticketing System, follow these steps:

### Input File:

Prepare an input file named **input.txt**. Each line in this file represents a command to be executed by the system. Commands include:

CREATECATEGORY Category_Name RowsxColumns

SELLTICKET Customer_Name Ticket_Type Category_Name Seat(s)

CANCELTICKET Category_Name Seat(s)

BALANCE Category_Name

SHOWCATEGORY Category_Name

### Example:

CREATECATEGORY category-1D 5x5

SELLTICKET ahmet full category-1D A1

SHOWCATEGORY category-1D

BALANCE category-1D

CANCELTICKET category-1D A1

### Execute Script:

Run the Python script:

```bash
python Assignment3.py input.txt
