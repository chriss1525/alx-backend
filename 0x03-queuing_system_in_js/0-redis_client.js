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
