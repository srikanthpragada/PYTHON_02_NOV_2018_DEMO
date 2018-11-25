create table products
(
 prodid   integer primary key AUTOINCREMENT,
 prodname text not null,
 price    integer not null,
 qoh      integer
 );


 insert into products(prodname,price,qoh)  values('iPhone X',90000,5);
 insert into products(prodname,price,qoh)  values('iPad Air 2',45000,12);
 insert into products(prodname,price,qoh)  values('One Plus 6T',35000,25);
 insert into products(prodname,price,qoh)  values('Hp Spectra Laptop',12000,3);
