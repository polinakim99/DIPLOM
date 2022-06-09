const container = document.querySelector('.container');
const seats = document.querySelectorAll('.row .seat:not(.occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');
const performSelect = document.getElementById('perform');

populateUI();

let ticketPrice = +performSelect.value;

// Save selected perform index and price
function setPerformData(performIndex, performPrice) {
  localStorage.setItem('selectedPerformIndex', performIndex);
  localStorage.setItem('selectedPerformPrice', performPrice);
}

// Update total and count
function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll('.row .seat.selected');

  const seatsIndex = [...selectedSeats].map(seat => [...seats].indexOf(seat));

  localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

  const selectedSeatsCount = selectedSeats.length;

  count.innerText = selectedSeatsCount;
  total.innerText = selectedSeatsCount * ticketPrice;

  setPerformData(performSelect.selectedIndex, performSelect.value);
}

// Get data from localstorage and populate UI
function populateUI() {
  const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));

  if (selectedSeats !== null && selectedSeats.length > 0) {
    seats.forEach((seat, index) => {
      if (selectedSeats.indexOf(index) > -1) {
        seat.classList.add('selected');
      }
    });
  }

  const selectedPerformIndex = localStorage.getItem('selectedPerformIndex');

  if (selectedPerformIndex !== null) {
    performSelect.selectedIndex = selectedPerformIndex;
  }
}

// perform select event
performSelect.addEventListener('change', e => {
  ticketPrice = +e.target.value;
  setPerformData(e.target.selectedIndex, e.target.value);
  updateSelectedCount();
});

// Seat click event
container.addEventListener('click', e => {
  if (
    e.target.classList.contains('seat') &&
    !e.target.classList.contains('occupied')
  ) {
    e.target.classList.toggle('selected');

    updateSelectedCount();
  }
});

// Initial count and total set
updateSelectedCount();
