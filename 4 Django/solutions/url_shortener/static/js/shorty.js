// const url = 'http://localhost:8000/shorten';

// $('#url-form').on('submit', (event) => {
//     event.preventDefault();

//     const user_url = $('#url-input').val();

//     axios.post('http://localhost:8000/shorten', {
//         user_url: user_url,
//         },
//         axios.defaults.xsrfCookieName = 'csrftoken',
//         axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
//     )
//     .then(response => {
//         $('#url-input').val('');
//         $('#url-input').focus();
//         $('#hash-display').text(response.message);
//     })
//     .catch(error => {
//         console.log(error);
//     })
// });

