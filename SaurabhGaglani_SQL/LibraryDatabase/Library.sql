/* Saurabh Gaglani */
CREATE TABLE  books
(
BookID int primary key, 
BookName Varchar(255),
GenreId varchar(255),
AuthorId int,
ReleaseYear int
);
CREATE TABLE Members
(
MemberID int primary key,
MemberName varchar(255),
MemberAddress varchar(255),
Age varchar(255)
);
CREATE TABLE borrowers(
MemberID int,
BookId int,
DateTaken varchar(255),
DateReturned varchar(255),
TimeOverdue int,
OverdueCosts int
);
CREATE TABLE genre(
GenreID int primary key,
GenreName varchar(255)
);
CREATE TABLE authors(
AuthorID int primary key,
AuthorName varchar(255)
);

insert into books values(1, 'The Karamazov Brothers', 1 , 1, 1880);
insert into books values(2, 'Crime and Punishment' , 1 , 1, 1866);
insert into books values(3, 'Jane Eyre' , 1 , 2, 1847);
insert into books values(4, 'Oliver Twist' , 1 , 3, 1839);
insert into books values(5, 'Wayne Rooney - My autobiography ' , 2 , 4, 1839);

insert into Members values(100, 'John L' ,'24 Dublin st Monaghan','Adult');
insert into Members values(101, 'Hugh O' ,'3 Cormac St Tullamore','Adult');
insert into Members values(102, 'James O' ,'43-45 Church St.','Adult');
insert into Members values(103, 'John O' ,'3 Eyre st Woodquay Galway','Child');
insert into members values(104, 'Chris G', 'Roden pl Dundalk','Child');

insert into borrowers values(100, 2 ,'24/10/2019','7/11/2019',null,null);
insert into borrowers values(101, 3 ,'6/4/2020','7/4/2020',null,null);
insert into borrowers values(102, 1 ,'8/5/2020','8/6/2020','15 days','10 euro' );
insert into borrowers values(103, '5' ,'8/5/2020', '9/6/2020','15 days', '10 euro');
insert into borrowers values(100, '5' ,'10/6/2020', '17/6/2020',null, null);

insert into genre values(1, 'Fiction');
insert into genre values(2, 'Biography');
insert into genre values(3, 'History' );
insert into genre values(4,'Romance');
insert into genre values(5, 'Science');

insert into authors values(1, 'Fyodor Dyostoevsky');
insert into authors values(2, 'Charolette Bronte');
insert into authors values(3, 'Charles Dickens' );
insert into authors values(4,'Wayne Rooney');
insert into authors values(5, 'William Shakespeare');

select *  from books;
select BookID,BookName from books;

select MemberName from members where age = 'Adult';
select MemberName,MemberAddress from members;

select * from borrowers where OverdueCosts is not null;
select sum(OverdueCosts) from borrowers;

select * from genre;
select GenreId from genre where GenreName = 'History';

select * from authors;
select AuthorId from authors where AuthorName = 'William Shakespeare';

select Members.MemberName, borrowers.OverdueCosts from Members 
inner join borrowers on Members.MemberID = borrowers.MemberID
where OverdueCosts is not null;

select borrowers.DateReturned, books.bookName from borrowers 
inner join books on borrowers.bookID = books.bookID;

select Members.MemberName, borrowers.DateReturned, books.bookName from(( borrowers
join books on borrowers.bookID = books.bookID) join members on Members.MemberID = borrowers.MemberID); 

select authors.AuthorName, Members.MemberName, borrowers.DateReturned, books.BookName from(( Authors
join books on Authors.AuthorID = books.AuthorID join borrowers on books.BookID = borrowers.BookID) join Members on Members.MemberID = borrowers.MemberID); 

select authors.AuthorName, Members.MemberName, borrowers.DateReturned, books.BookName, genre.GenreName from(( Authors
join books on Authors.AuthorID = books.AuthorID join borrowers on 
books.BookID = borrowers.BookID join genre on books.GenreID = genre.GenreId) 
join Members on Members.MemberID = borrowers.MemberID) 
where OverdueCosts is not null; 








