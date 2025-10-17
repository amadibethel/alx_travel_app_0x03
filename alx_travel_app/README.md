# ALX Travel App - Chapa Payment Integration

This project is a Django-based travel booking application integrated with the **Chapa Payment Gateway** for secure payment processing. Users can create bookings, make payments via Chapa, and have their payment statuses tracked automatically.

---

## **Project Overview**

The application demonstrates a real-world payment workflow including:

- Secure payment initiation using Chapa API.
- Verification of payment status.
- Automatic updating of payment status in the database.
- Optional email notifications for successful payments using Celery.

---

## **Features**

- **Secure Payment Initiation:** Users are redirected to Chapa checkout pages.
- **Payment Verification:** Payments are verified automatically with Chapa.
- **Payment Status Tracking:** The `Payment` model tracks `Pending`, `Completed`, and `Failed` transactions.
- **Error Handling:** Failed payments are logged and gracefully handled.
- **Sandbox Testing:** Payments can be tested using Chapa’s sandbox environment.

---

## **Setup Instructions**

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/alx_travel_app_0x02.git
cd alx_travel_app_0x02

