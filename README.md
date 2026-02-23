# Ticket Booking API Documentation

## Overview
This documentation provides comprehensive details about the Ticket Booking API, including its endpoints, request/response structures, edge cases, and testing instructions.  

## Prompt Engineering Iterations
- **Iteration 1:** Initial API design focused on basic ticket booking functionalities.
- **Iteration 2:** Added user authentication and authorization features.
- **Iteration 3:** Improved error handling and added edge case scenarios.

## API Endpoints

### 1. Create Booking
- **Endpoint:** `/api/bookings`
- **Method:** POST
- **Parameters:**  
  - `user_id` (required): ID of the user making the booking  
  - `event_id` (required): ID of the event for which ticket is being booked  
  - `num_tickets` (required): Number of tickets to book  
- **Success Response:**  
  - **Code:** 201  
  - **Content:** `{ "message": "Booking created successfully", "booking_id": "12345" }`

### 2. Get Booking Details
- **Endpoint:** `/api/bookings/{booking_id}`
- **Method:** GET
- **Parameters:**  
  - `booking_id` (required): The ID of the booking to retrieve  
- **Success Response:**  
  - **Code:** 200  
  - **Content:** `{ "booking_id": "12345", ... }`

### 3. Cancel Booking
- **Endpoint:** `/api/bookings/{booking_id}`
- **Method:** DELETE
- **Parameters:**  
  - `booking_id` (required): The ID of the booking to cancel  
- **Success Response:**  
  - **Code:** 200  
  - **Content:** `{ "message": "Booking cancelled successfully" }`

## Edge Cases
- Attempting to book more tickets than available.
- Booking for an event that does not exist.
- Cancelling a booking that does not belong to the user.

## Testing Instructions
1. **Setup:** Clone the repository and install the required dependencies.
2. **Run Tests:** Execute the test suite using the command `npm test`.
3. **Postman Collection:** Use the provided Postman collection to test the API endpoints easily.

## Conclusion
This documentation should serve as a guideline for both developers and testers working with the Ticket Booking API. Please ensure to keep this updated with any changes in functionality or additional endpoints.