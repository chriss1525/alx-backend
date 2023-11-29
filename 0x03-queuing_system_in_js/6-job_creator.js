// use kue to create a queue

import { createQueue} from 'kue';

const queue = createQueue();

const jobData = queue.create('push_notification_code', {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}).save((err) => {
  if (!err) console.log(`Notification job created: ${jobData.id}`);
}
);

jobData.on('complete', () => {
  console.log('Notification job completed:', jobData.id);
}
);

jobData.on('failed', (err) => {
  console.log('Notification job failed:', jobData.id);
}
);
