echo "----------------------------------\n"
echo "Check that the clients are there.\n"
echo "----------------------------------\n"
curl -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/clients/
echo "---------------------------------------\n"
echo "Check that the product areas are there.\n"
echo "---------------------------------------\n"
curl -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/product-areas/
echo "----------------------------\n"
echo "Create the feature requests.\n"
echo "----------------------------\n"
curl --data "id=1&title='feature foo'&description='it must have this bogus'&client=1&client_priority=1&target_date=1987-09-03 00:00&ticket_uri='http://foo.com'
&product_areas=1" -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/feature-requests/
echo "--------------------------------------------\n"
echo "Check that the new feature request is there.\n"
echo "--------------------------------------------\n"
curl  -H 'Accept: application/json; indent=4' -u admin:Password http://127.0.0.1:8080/feature-requests/
