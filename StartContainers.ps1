Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\backend\servicedelivery
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\backend\singleview
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\ldapserver
docker container start apacheds
echo " - Container apacheds  Started"

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_db
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_accounts
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_assets
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_orders
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_invoices
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_service_requests
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_activities
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\microservice\oach_cti
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0\frontend\oach_ui
docker compose start

Set-Location C:\Users\mukul\Documents\OACH\OACH_v2.0

docker ps