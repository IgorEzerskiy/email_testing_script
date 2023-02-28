#!/bin/bash
test='command.php'
command='Mail::raw("'$1'", function($msg) {$msg->to("'$2'")->subject("'$3'"); });'

echo $command
echo $1
echo $2
echo $3
cd /home/igor/prj/ground
docker-compose exec -u root -T php touch $test
docker-compose exec -u root -T php echo $command >> $test
docker-compose exec -u root -T php more $test | docker-compose exec -u root -T php php artisan tinker
sudo docker-compose exec -u root -T php rm $test
