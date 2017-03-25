create database productos

use productos;

create table producto(
id_producto mediumint (8) not null auto_increment,
nombre varchar (20) not null,
descripcion varchar (22) not null,
existencias int (5) not null,
precio_compra float (5) not null,
precio_venta float (5) not null,
imagen_producto varchar(100) not null,
PRIMARY KEY (id_producto)
);

insert into producto values ("1","mayonesa","tarro grande","2","20.5","25.5");
insert into producto values ("2","helado","vainilla rico","2","20.5","25.5");

select * from producto;
