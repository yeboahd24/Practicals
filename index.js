const API_URL = 'https://api.example.com/jobs';
const resultsContainer = document.querySelector('#results');

// Fetch job data from the API
async function getJobs(query) {
  const res = await fetch(`${API_URL}?q=${query}`);
  const data = await res.json();
  return data;
}

// Display the job data in the results container
function displayJobs(jobs) {
  // Clear the previous results
  resultsContainer.innerHTML = '';

  // Loop through the jobs and add them to the results container
  jobs.forEach(job => {
    const result = document.createElement('div');
    result.classList.add('bg-white', 'rounded', 'shadow', 'p-4', 'mb-4');
    result.innerHTML = `
      <h2 class="text-xl font-bold mb-2"><a href="${job.url}">${job.title}</a></h2>
      <p class="text-gray-700 mb-2"><a href="${job.company.url}">${job.company.name}</a></p>
      <p class="text-gray-700 mb-2">${job.location}</p>
    `;
    resultsContainer.appendChild(result);
  });
}

// Search for jobs when the form is submitted
const searchForm = document.querySelector('#search-form');
searchForm.addEventListener('submit', event => {
  event.preventDefault();
  const title = searchForm.querySelector('input[name="title"]').value;
  const location = searchForm.querySelector('input[name="location"]').value;
  getJobs(title, location).then(displayJobs);
});
