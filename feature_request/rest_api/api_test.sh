echo "-------------------\n"
echo "Create the clients.\n"
echo "-------------------\n"
curl --data "name=ClientA" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/clients/
curl --data "name=ClientB" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/clients/
curl --data "name=ClientC" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/clients/
echo "----------------------------------\n"
echo "Check that the clients are there.\n"
echo "----------------------------------\n"
curl -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/clients/
echo "-------------------------\n"
echo "Create the product areas.\n"
echo "-------------------------\n"
curl --data "name=Policies" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/product-areas/
curl --data "name=Billing" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/product-areas/
curl --data "name=Clains" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/product-areas/
curl --data "name=HumanResources" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/product-areas/
echo "---------------------------------------\n"
echo "Check that the product areas are there.\n"
echo "---------------------------------------\n"
curl -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/product-areas/
echo "----------------------------\n"
echo "Create the feature requests.\n"
echo "----------------------------\n"
curl --data "title='feature foo'&description='it must have this'&client=ClientA&client_priority=1&target_date=10/06/2016&ticket_url='http://foo.com'&product_areas=Policies" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/feature-requests/
echo "--------------------------------------------\n"
echo "Check that the new feature request is there.\n"
echo "--------------------------------------------\n"
curl  -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/feature-requests/
