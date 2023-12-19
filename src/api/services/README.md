Controllers SHOULD NOT have very much logic AT ALL within them.
Create Services to manage the complexity that you would usually fit into an api endpoint.

Don't box yourself in! Maybe you need 1 service, maybe you need 20. As long as the code is
appropriately de-coupled, it will be easier to work with than 1 huge file.
