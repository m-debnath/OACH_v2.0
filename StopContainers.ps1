Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\frontend\oach_ui
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_cti
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_accounts
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_assets
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_orders
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_invoices
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_service_requests
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_activities
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_db
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\ldapserver
docker container stop apacheds
echo " - Container apacheds  Stopped"

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\backend\servicedelivery
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\backend\singleview
docker compose stop

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0

docker ps