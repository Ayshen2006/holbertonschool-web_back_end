import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      const result = `${photo.body} ${user.firstName} ${user.lastName}`;
      console.log(result);
      return result;
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
