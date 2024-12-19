Instead of calculating checksum for whole table, we can optimise by applying for only rows. This will reduce the sorting step.

![Screenshot 2024-12-20 at 1 39 58 AM](https://github.com/user-attachments/assets/052e3b3a-c365-4d26-b894-f7b1de030902)

What if we have billions of records?????
We can do db partitioning on the basis of indexes or primary key etc. then apply checksum for particular row.
