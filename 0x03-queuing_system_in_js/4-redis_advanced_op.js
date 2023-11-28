// store a hash value using hset

var redis = require('redis');
import { createClient } from 'redis';

var client = createClient();

client.on('error', function(err) {
  console.log('Redis client not connected to the server: ' + err);
});

const updateHash = (hashName, fieldName, value) => {
  client.hset(hashName, fieldName, value, redis.print);
};

const printHash = (hashName) => {
  client.hgetall(hashName, (err, res) => {
    console.log(res);
  });
}

const obj = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const key in obj) {
  updateHash('HolbertonSchools', key, obj[key]);
}

printHash('HolbertonSchools');


