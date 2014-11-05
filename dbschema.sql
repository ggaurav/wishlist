#item_type = electronics/clothing
#assuming a single currency, otherwise we could add a field for currency
#status to handle out of stock items
CREATE TABLE `items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `description` text,
  `item_type` varchar(500) DEFAULT NULL,
  `cost` decimal(10,2) DEFAULT NULL,  
  `lastModified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` int(11) DEFAULT '0',
  `img` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

#we could also have a field named count to handle cases when a user wants to add more than 1 copy of a same item.
CREATE TABLE `wishlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_item` (`item_id`, `user_id`)  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

#insert into items values (null, 'item 1', 'blah blah', 'electronics', 20.5, null, '1','http://macbookpro.photorecoveryrmac1.com/files/2013/07/MacBookPro.jpg');
#insert into items values (null, 'item 2', 'blah blah', 'travel', 20.5, null, '1','http://static.in.groupon-content.net/93/28/1364370042893.jpg');
#insert into items values (null, 'item 3', 'blah blah', 'food', 20.5, null, '1','http://i.telegraph.co.uk/multimedia/archive/01807/bread_1807973b.jpg');
#insert into items values (null, 'item 4', 'blah blah', 'electronics', 20.5, null, '1','http://cdn.pocket-lint.com/r/s/628x/assets/images/phpsryjtf.jpg');
