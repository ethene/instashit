#!/bin/bash
echo omgwtfk - app
curl -D heads https://api.instagram.com/v1/users/211585314/media/recent/?access_token=398903202.249fcce.3b3c4532d63646ed83b11046a58ea054 >/dev/null
echo \n
grep "X-Ratelimit" heads

curl -D heads -F 'access_token=398903202.249fcce.3b3c4532d63646ed83b11046a58ea054' \
    https://api.instagram.com/v1/media/376033959341256322_211585314/likes
echo \n
grep "X-Ratelimit" heads
#echo 3th3n3 - testapp
#curl -D heads -X POST -d "action=follow" https://api.instagram.com/v1/users/331762741/relationship?access_token=211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562
#echo \n
#grep "X-Ratelimit" heads
#echo sorryiamnot - 3th3n3 - testapp
#curl -D heads -X POST -d "action=follow" https://api.instagram.com/v1/users/211585314/relationship?access_token=331762741.e1b377f.ae281d5df63f4cb0996940d707c2df39
#echo \n
#grep "X-Ratelimit" heads
rm heads



