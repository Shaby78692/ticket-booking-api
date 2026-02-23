import threading
import time
import unittest

class TicketBooking:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.lock = threading.Lock()

    def book_ticket(self, tickets):
        with self.lock:
            if tickets <= self.total_tickets:
                time.sleep(0.1)  # Simulate processing time
                self.total_tickets -= tickets
                return True
            return False

class TestTicketBooking(unittest.TestCase):
    def setUp(self):
        self.booking_system = TicketBooking(10)  # Total 10 tickets available

    def test_double_booking_prevention(self):
        result1 = self.booking_system.book_ticket(5)
        result2 = self.booking_system.book_ticket(5)
        self.assertTrue(result1)
        self.assertFalse(result2)  # Should fail due to double booking

    def test_rate_limiting(self):
        threads = []
        for _ in range(5):
            t = threading.Thread(target=self.booking_system.book_ticket, args=(3,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(self.booking_system.total_tickets, 0)  # All tickets should be booked

    def test_concurrent_bookings(self):
        threads = []
        for _ in range(3):
            t = threading.Thread(target=self.booking_system.book_ticket, args=(5,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(self.booking_system.total_tickets, 0)  # Should be fully booked

    def test_input_validation(self):
        self.assertFalse(self.booking_system.book_ticket(15))  # Not enough tickets
        self.assertTrue(self.booking_system.book_ticket(5))  # Should succeed
        self.assertEqual(self.booking_system.total_tickets, 5) # 10 - 5 = 5 tickets left

if __name__ == '__main__':
    unittest.main()