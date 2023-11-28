// connect to redis server
// log Redis client connected to the server on success
// log Redis client connected to the server on error

import { createClient } from 'redis';
import redis from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
}
);

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
}
);

// function that sets the value of the key schoolName
// display a confirmation message using the redis.print function

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

// function that displays the value of the key schoolName

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
