// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div>
//       sddgdjfkdhj
//     </div>
//   );
// }

// export default App;


import React, { useState } from 'react';
import './App.css';

function App() {
  const [bookedSlots, setBookedSlots] = useState([]);
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [selectedTimeSlot, setSelectedTimeSlot] = useState('');

  // Function to book a slot
  const bookSlot = () => {
    // Check if a time slot is selected
    if (!selectedTimeSlot) {
      alert('Please select a time slot.');
      return;
    }

    // Check if the selected time slot is in the past
    if (new Date(selectedTimeSlot) <= new Date()) {
      alert('You cannot book a slot in the past.');
      return;
    }

    // Book the slot
    setBookedSlots([...bookedSlots, selectedTimeSlot]);
    setSelectedTimeSlot('');
  };

  // Function to render time slots
  const renderTimeSlots = () => {
    const currentTime = new Date();
    currentTime.setMinutes(0, 0, 0); // Set minutes and seconds to 0 for precise comparison
    const timeSlots = [];

    // Generate time slots from 9:00 AM to 5:00 PM
    for (let i = 9; i <= 17; i++) {
      const slotTime = new Date(selectedDate);
      slotTime.setHours(i, 0, 0, 0);

      // Check if the slot is already booked or in the past
      if (!bookedSlots.includes(slotTime.toString()) && slotTime > currentTime) {
        timeSlots.push(
          <option key={slotTime.toString()} value={slotTime.toString()}>
            {slotTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </option>
        );
      }
    }

    return timeSlots;
  };

  return (
    <div className="App">
      <h1>Booking Calendar</h1>
      <div>
        <label>Select a date:</label>
        <input type="date" value={selectedDate.toISOString().slice(0, 10)} onChange={(e) => setSelectedDate(new Date(e.target.value))} />
      </div>
      <div>
        <label>Select a time slot:</label>
        <select value={selectedTimeSlot} onChange={(e) => setSelectedTimeSlot(e.target.value)}>
          <option value="">-- Select a time slot --</option>
          {renderTimeSlots()}
        </select>
      </div>
      <button onClick={bookSlot}>Book Slot</button>
      <div>
        <h2>Booked Slots</h2>
        <ul>
          {bookedSlots.map((slot, index) => (
            <li key={index}>{new Date(slot).toLocaleString()}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;