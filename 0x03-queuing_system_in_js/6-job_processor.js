// create a new queue

const redis = require('redis');
import { createQueue } from 'kue';

const queue = createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// process jobs
queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
