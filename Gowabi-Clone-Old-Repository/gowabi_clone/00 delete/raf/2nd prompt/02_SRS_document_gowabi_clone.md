# **Spa-salon booking and management application**


## **Supported URLs**
[01. Web site structure on Figma](https://www.figma.com/board/du3f45TFQTuV3S2UF4AkBC/Gowabi-clone-website-structure?node-id=0-1&t=VUDNlDDcPwZWM1QV-1)


## **System Overview**
```
The application goal is to streamline operations, improve customer service,
and increase sales for spas & salons small business owners.

The project is about to create a spa/salon booking & management system (similar to GoWabi.com) with a design like Yelp for the US market.
This system will help spa and salon owners manage their business better,
make it easy for customers to book appointments online, and improve communication.
```

## **High level features of the System**
```
1. Service Booking: Find and book wellness and beauty services.
2. Multi-Payment: Pay with card, PayPal, etc.
3. Appointment: Book and manage appointments online.
4. Customer Profiles: Keep customer details and history.
5. Vendor Profiles: Manage business info and services.
6. Staff: Schedule and track employee work.
7. Business Tools: Manage salons and clinics smoothly.
8. Customer Messages: Auto reminders, feedback, and promotions.
9. Inventory: Track and manage stock easily.
10. Reports: Get reports to improve business.
11. POS: Easy sales with POS integration.
12. CRM: Integrated customer management.
```


## **Stakeholder of the system**
```
1. Spa or other service user
2. Spa service or other service owner
3. Spa service or other service employees
4. System Admin
5. Developer
6. 3rd-party services
7. Owner of the business
```


## **User Stories**
<br>

## **Feature 1: Service Booking: Find and book wellness and beauty services.**

```
1. As a customer,
I want to search for wellness and beauty services based on my current location. So that I can easily find services nearby.
        A. The system detects the customer's location or allows manual input.
        B. The customer is shown a list of services available within a specified radius.

2. As a customer,
I want to filter the services by categories such as massage, facial, or hair care, so that I can quickly find the type of service I’m interested in.
Categories are displayed prominently as filters.
        A. Customers can select one or multiple categories.
        B. The service list updates in real-time to reflect the selected categories.

3. As a customer,
I want to sort services by price, rating, and distance so that I can prioritize services that match my preferences.
        A. Sorting options include price (low to high, high to low), rating, and distance.
        B. The system displays sorted results based on the selected option.

4. As a customer,
I want to view detailed information about a service, including descriptions, prices, durations, and customer reviews so that I can make an informed decision.
        A. Service detail pages include comprehensive information such as service name, description, price, duration, provider information, and customer reviews.
        B. The page is accessible from the search results or service listings.


5. As a customer,
I want to see a list of available timeslots for a service so that I can choose a convenient time for my appointment.
        A. Available timeslots are shown on the service detail page.
        B. The customer can select a timeslot and proceed to booking.

6. As a customer,
I want to book a service by selecting an available timeslot and providing my contact information so that I can secure my appointment.
        A. The booking process includes timeslot selection, contact information entry, and confirmation.
        B. The system confirms the booking and provides a summary of the appointment details.

7. As a customer,
I want to receive a confirmation email or SMS with the appointment details so that I have a record of my booking.
        A. After booking, the system sends a confirmation to the customer via email or SMS.
        B. The confirmation includes the service details, time, date, and location.

‭8.‬ ‭As a customer,
I want to be able to view and manage my upcoming appointments through a ‘My‬
‭Bookings’ section so that I can keep track of my schedules.‬
‭	a.‬ ‭The customer can access a 'My Bookings' section from their profile.‬
‭	b.‬ ‭The section lists all upcoming and past appointments with options to view details, cancel,‬ or reschedule.‬


‭9.‬ ‭As a customer,
I want to cancel or reschedule my appointment if needed so that I can manage‬
‭changes in my schedule.‬
‭a.‬ ‭The customer can select an appointment to cancel or reschedule from 'My Bookings.'‬
‭b.‬ ‭The system updates the booking status and sends a notification of the change to both the‬
‭customer and the service provider.‬

‭10.‬ ‭As a customer,
I want to leave a review and rating after my appointment so that I can share‬
‭my experience with others.‬
‭a.‬ ‭The system prompts the customer to leave a review after the appointment.‬
‭b.‬ ‭The customer can rate the service and write a review, which is then displayed on the‬
‭service provider's profile.‬

‭11.‬‭As a vendor,
I want to manage my list of services and their descriptions so that customers‬
‭always see up-to-date and accurate information.‬
‭a.‬ ‭The vendor can log in to their profile and update service details, prices, and availability.‬
‭b.‬ ‭Changes are reflected immediately on the customer-facing service listings.‬

‭12.‬ ‭As a vendor,
I want to set and manage my available timeslots so that customers can only‬
‭book when I am available.‬
‭a.‬ ‭The vendor can update their availability on a calendar interface.‬
‭b.‬ ‭Only available timeslots are shown to customers during the booking process.‬

‭13.‬ ‭As a vendor,
I want to receive notifications of new bookings and cancellations so that I can‬
‭manage my schedule efficiently.‬
‭a.‬ ‭The vendor receives real-time notifications via email or SMS for every new booking or‬
‭cancellation.‬
‭b.‬ ‭Notifications include appointment details such as customer name, service booked, date,‬
‭and time.‬

‭14.‬ ‭As a vendor,
I want to view and manage all upcoming appointments through a dashboard so‬
‭that I can prepare for each customer.‬
‭a.‬ ‭The dashboard displays a list of all upcoming appointments with relevant details.‬
‭b.‬ ‭The vendor can update the status of appointments (e.g., completed, canceled).‬

‭15.‬ ‭As a vendor,
I want to block out times when I'm unavailable (e.g., holidays, personal time) so‬
‭that customers cannot book during those periods.‬
‭a.‬ ‭The vendor can block out specific dates and times in their availability settings.‬
‭b.‬ ‭The system ensures these blocked times are not available for booking.‬
```


## **‭Feature 2: Multi-Payment: Pay with card, PayPal, etc.‬**
```
‭1)‬ ‭As a customer,
I want to select my preferred payment method (e.g., credit card, PayPal, etc.)‬
‭during the booking process so that I can pay using the method that is most convenient for me.‬
‭a)‬ ‭The payment options include credit/debit card, PayPal, and other supported methods.‬
‭b)‬ ‭The selected payment method is used to process the transaction.‬

‭2)‬ ‭As a customer,
I want to securely store my payment details for future bookings so that I can‬
‭check out more quickly next time.‬
‭a)‬ ‭The system offers an option to save payment details during checkout.‬
‭b)‬ ‭Saved payment methods can be managed in the customer’s profile, with options to add,‬
‭remove, or update.‬

‭3)‬ ‭As a customer,
I want to see the total amount to be paid, including taxes, discounts, and any‬
‭additional fees, before confirming my booking so that I have a clear understanding of the costs.‬
‭a)‬ ‭The booking summary displays a detailed breakdown of charges, including the base price,‬
‭taxes, any applied discounts, and total payable amount.‬
‭b)‬ ‭The customer must confirm the total before proceeding to payment.

‭4)‬ ‭As a customer,
I want to apply a promotional code or discount voucher during payment so that I‬
‭can receive a discount on my booking.‬
‭a)‬ ‭The payment screen includes an option to enter a promo code or voucher.‬
‭b)‬ ‭The system validates the code and applies the discount to the total amount.‬
‭
5)‬ ‭As a customer,
I want to receive a confirmation email or SMS after payment is successfully‬
‭processed so that I have a receipt for my transaction.‬
‭a)‬ ‭Upon successful payment, the system sends a confirmation via email or SMS.‬
‭b)‬ ‭The receipt includes booking details, payment amount, and transaction ID.‬

‭6)‬ ‭As a customer,
I want to view my payment history in my profile so that I can keep track of all my‬
‭transactions.‬
‭a)‬ ‭The customer’s profile includes a 'Payment History' section.‬
‭b)‬ ‭This section lists all past payments with details like date, amount, and payment method‬
‭used.‬

‭7)‬ ‭As a customer,
I want to be able to cancel a booking and request a refund if eligible so that I can‬
‭get my money back according to the cancellation policy.‬
‭a)‬ ‭The cancellation policy is clearly stated during the booking process.‬
‭b)‬ ‭Eligible cancellations trigger a refund process, and the system informs the customer about‬
‭the refund timeline.‬

‭8)‬ ‭As a vendor,
I want to receive notifications of successful payments so that I can confirm that a‬
‭booking has been paid for.‬
‭a)‬ ‭The vendor is notified immediately after a customer’s payment is processed.‬
‭b)‬ ‭Notifications include the payment method used and the total amount received.‬
‭
9)‬ ‭As a vendor, I want to view a summary of all payments received within a specific period so that I‬
‭can reconcile my accounts.‬
‭a)‬ ‭The vendor can generate a report of payments received, filtered by date range.‬
‭b)‬ ‭The report includes details like payment method, amount, and associated bookings.‬

‭10)‬ ‭As a vendor,
I want to manage accepted payment methods for my services so that I can‬
‭control which payment options are available to customers.‬
‭a)‬ ‭The vendor can enable or disable specific payment methods from their profile settings.‬
‭b)‬ ‭The system only shows enabled payment methods to customers during checkout.‬
‭
11)‬ ‭As a vendor,
I want to handle partial payments or deposits so that customers can secure a‬
‭booking by paying a portion of the total amount upfront.‬
‭a)‬ ‭The vendor can set up partial payment options for specific services.‬
‭b)‬ ‭The system calculates the deposit amount and collects the remaining balance at a later‬
‭time.‬

‭12)‬ ‭As a vendor,
I want to offer installment payment options (e.g., Buy Now, Pay Later) so that‬
‭customers can spread the cost of their booking over time.‬
‭a)‬ ‭The vendor can integrate installment payment options like BNPL (Buy Now, Pay Later)‬
‭into their payment system.‬
‭b)‬ ‭Customers are informed about the installment terms before choosing this option.‬

‭13)‬ ‭As a vendor,
I want to refund a customer directly through the system if needed so that the‬
‭refund process is quick and easy.‬
‭a)‬ ‭The vendor can initiate a refund from their payment management dashboard.‬
‭b)‬ ‭The system processes the refund and updates the customer’s payment history‬
‭accordingly.‬
‭
14)‬ ‭As a vendor,
I want to set up automatic payment reminders for customers so that they are‬
‭reminded to pay any outstanding balances.‬
‭a)‬ ‭The vendor can configure automatic reminders for unpaid balances.‬
‭b)‬ ‭The system sends reminders via email or SMS according to the vendor’s settings.‬
‭
15)‬ ‭As a system admin,
I want to manage the integration with payment gateways so that all‬
‭transactions are secure and compliant with industry standards.‬
‭a)‬ ‭The admin can add or update payment gateways in the system’s backend.‬
‭b)‬ ‭The system ensures all transactions are processed securely and comply with PCI-DSS‬
‭standards.‬
```

## **‭Feature 3: Appointment: Book and manage appointments online.‬**
```
‭1)‬ ‭As a customer,
I want to view available time slots for a specific service so that I can choose a‬
‭convenient time for my appointment.‬
‭a)‬ ‭The system displays available time slots based on the selected service and provider.‬
‭b)‬ ‭Time slots are updated in real-time to reflect any changes in availability.‬
‭
2)‬ ‭As a customer,
I want to book an appointment by selecting a service, provider, and time slot so‬
‭that I can schedule my visit easily.‬
‭a)‬ ‭The booking process allows the customer to select a service, provider, and time slot.‬
‭b)‬ ‭The system confirms the appointment and provides a summary of the booking.‬
‭
3)‬ ‭As a customer,
I want to receive an appointment confirmation email or SMS so that I have a‬
‭record of my booking.‬
‭a)‬ ‭Upon successful booking, the system sends a confirmation via email or SMS.‬
‭b)‬ ‭The confirmation includes service details, provider information, time, and date.‬

‭4)‬ ‭As a customer,
I want to view all my upcoming and past appointments in a 'My Appointments'‬
‭section so that I can manage my schedule.‬
‭a)‬ ‭The 'My Appointments' section lists all upcoming and past appointments.‬
‭‭b)‬ ‭The customer can view appointment details, including service, provider, and time.‬

‭5)‬ ‭As a customer,
I want to be able to reschedule an existing appointment if my plans change so‬
‭that I can adjust my booking to a more suitable time.‬
‭a)‬ ‭The customer can select an existing appointment and choose a new time slot.‬
‭b)‬ ‭The system updates the appointment details and sends a confirmation of the reschedule.‬
‭
6)‬ ‭As a customer,
I want to cancel an appointment if I can no longer attend so that the time slot is‬
‭freed up for others.‬
‭a)‬ ‭The customer can cancel an appointment from the 'My Appointments' section.‬
‭b)‬ ‭The system processes the cancellation and notifies the provider of the change.‬
‭
7)‬ ‭As a customer,
I want to receive reminders via email or SMS before my appointment so that I‬
‭don’t forget about it.‬
‭a)‬ ‭The system sends reminders at configurable intervals (e.g., 24 hours, 1 hour) before the‬
‭appointment.‬
‭b)‬ ‭Reminders include service details, time, and location.‬
‭
8)‬ ‭As a vendor,
I want to set up my availability and time slots so that customers can only book‬
‭appointments when I’m free.‬
‭a)‬ ‭The vendor can manage their availability through a calendar interface.‬
‭b)‬ ‭Only available time slots are shown to customers during the booking process.‬
‭
9)‬ ‭As a vendor,
I want to view all upcoming appointments in a daily, weekly, or monthly view so that‬
‭I can plan my schedule efficiently.‬
‭a)‬ ‭The vendor’s dashboard includes calendar views (daily, weekly, monthly) of upcoming‬
‭appointments.‬
‭b)‬ ‭Each appointment entry includes details such as customer name, service, and time.‬
‭
10)‬ ‭As a vendor,
I want to receive notifications of new appointments, reschedules, and‬
‭cancellations so that I am always aware of changes in my schedule.‬
‭a)‬ ‭The vendor receives real-time notifications via email or SMS for new appointments,‬
‭reschedules, and cancellations.‬
‭b)‬ ‭Notifications include relevant details such as customer name, service, and time.‬

‭11)‬ ‭As a vendor,
I want to block out specific dates or times (e.g., holidays, personal time) so that‬
‭customers cannot book appointments during those periods.‬
‭a)‬ ‭The vendor can block out time slots directly from their availability calendar.‬
‭b)‬ ‭Blocked time slots are not available for customer bookings.‬

‭12)‬ ‭As a vendor,
I want to set up appointment buffers (e.g., 15 minutes between appointments)‬
‭so that I have time to prepare for the next customer.‬
‭a)‬ ‭The vendor can configure buffer times between appointments.‬
‭b)‬ ‭The system ensures that buffer times are automatically included in the vendor's schedule.‬

‭13)‬ ‭As a vendor,
I want to limit the number of appointments I can accept in a day so that I don’t‬
‭overbook myself.‬
‭a)‬ ‭The vendor can set a maximum number of appointments per day.‬
‭b)‬ ‭Once the limit is reached, the system prevents further bookings for that day.‬
‭
14)‬ ‭As a vendor,
I want to customize the services I offer during specific time slots so that I can‬
‭allocate time for different types of services.‬
‭a)‬ ‭The vendor can specify which services are available during particular time slots.‬
‭b)‬ ‭The system only shows the available services to customers based on the time slot‬
‭selected.‬
‭
15)‬ ‭As a system admin,
I want to manage and monitor all appointments across the platform so‬
‭that I can ensure the system is functioning smoothly.‬
‭a)‬ ‭The admin dashboard includes tools to view, filter, and manage appointments across all‬
‭vendors and customers.‬
‭b)‬ ‭The system logs all appointment activities for auditing and troubleshooting purposes.‬
‭
16)‬ ‭As a vendor,
I want to be able to manually add or adjust appointments directly through the‬
‭system so that I can accommodate walk-ins or special requests.‬
‭a)‬ ‭The vendor can manually add appointments to their calendar or adjust existing bookings.‬
‭b)‬ ‭Manually added appointments are integrated into the vendor’s schedule and are visible in‬
‭the system.‬
```


## **‭‭Feature 4: Customer Profiles: Keep customer details and history.‬‬**
```
‭1)‬ ‭As a customer,
I want to create a profile with my personal information (name, email, phone‬
‭number) so that I can easily book services and receive notifications.‬
‭a)‬ ‭The system allows customers to create a profile by entering their name, email, and phone‬
‭number.‬
‭b)‬ ‭The profile is stored securely, and the customer receives a confirmation upon successful‬
‭creation.‬
‭
2)‬ ‭As a customer,
I want to update my personal information (e.g., change of address, phone‬
‭number) so that my profile remains accurate.‬
‭a)‬ ‭The customer can edit their profile details at any time.‬
‭b)‬ ‭The system validates and saves the updated information.‬

‭3)‬ ‭As a customer,
I want to view my booking history so that I can keep track of the services I have‬
‭used.‬
‭a)‬ ‭The 'My Profile' section includes a history of all past bookings.‬
‭b)‬ ‭Each entry in the history includes service details, date, provider, and status (e.g.,‬
‭completed, canceled).‬
‭
4)‬ ‭As a customer,
I want to save my favorite services and providers so that I can quickly access‬
‭and rebook them in the future.‬
‭a)‬ ‭The system allows customers to add services and providers to a 'Favorites' list.‬
‭b)‬ ‭The 'Favorites' list is easily accessible from the customer’s profile.‬
‭
5)‬ ‭As a customer,
I want to store multiple payment methods in my profile so that I can choose‬
‭between them when making a booking.‬
‭a)‬ ‭The system supports the addition of multiple payment methods (e.g., credit card, PayPal).‬
‭b)‬ ‭The customer can manage (add, delete, update) these payment methods from their‬
‭profile.‬
‭
6)‬ ‭As a customer,
I want to set my communication preferences (e.g., email, SMS) so that I receive‬
‭notifications in the way that I prefer.‬
‭a)‬ ‭The profile settings include options to choose preferred communication methods.‬
‭b)‬ ‭The system sends notifications based on the selected preferences.‬
‭
7)‬ ‭As a customer,
I want to securely save my login credentials (e.g., email and password) so that I‬
‭can easily access my account in the future.‬
‭a)‬ ‭The system supports secure storage of login credentials with options to reset or change‬
‭passwords.‬
‭b)‬ ‭The customer can enable two-factor authentication (2FA) for added security.‬
‭
8)‬ ‭As a customer,
I want to manage my notifications (e.g., reminders, promotions) so that I can‬
‭control the type and frequency of messages I receive.‬
‭a)‬ ‭The profile settings include options to manage notification preferences (e.g., appointment‬
‭reminders, promotional offers).‬
‭b)‬ ‭The customer can opt in or out of specific types of notifications.‬
‭
9)‬ ‭As a customer,
I want to view and download my payment receipts from past bookings so that I‬
‭have a record of my transactions.‬
‭a)‬ ‭The 'Payment History' section in the customer profile includes options to view and‬
‭download receipts.‬
‭b)‬ ‭Each receipt includes booking details, payment method, and total amount.‬

‭10)‬ ‭As a customer,
I want to delete my profile and all associated data if I no longer wish to use‬
‭the service so that my information is removed from the system.‬
‭a)‬ ‭The system provides an option to delete the customer’s profile, including all personal‬
‭information and booking history.‬
‭b)‬ ‭The deletion process is confirmed via email or SMS before the profile is permanently‬
‭removed.‬

‭11)‬‭As a vendor,
I want to view customer profiles, including their booking history and preferences,‬
‭so that I can provide personalized services.‬
‭a)‬ ‭Vendors can access customer profiles through their dashboard.‬
‭b)‬ ‭The profile includes booking history, service preferences, and any saved payment‬
‭methods (with sensitive information masked).‬
‭
12)‬ ‭As a vendor,
I want to add notes to customer profiles (e.g., preferences, special requests) so‬
‭that I can provide better service in future appointments.‬
‭a)‬ ‭The vendor can add private notes to customer profiles, visible only to the vendor.‬
‭b)‬ ‭Notes can be updated or deleted as needed and are accessible when viewing the‬
‭customer’s upcoming bookings.‬
‭
13)‬ ‭As a vendor,
I want to see customer ratings and feedback left by them after previous‬
‭appointments so that I can improve my services.‬
‭a)‬ ‭Customer profiles include a section for ratings and feedback they have provided.‬
‭b)‬ ‭The vendor can view this feedback and use it to make adjustments to their services.‬
‭
14)‬ ‭As a system admin,
I want to ensure that customer profiles are secure and compliant with‬
‭data protection regulations (e.g., GDPR) so that customer data is handled responsibly.‬
‭a)‬ ‭The system enforces data encryption and secure access controls for all customer profiles.‬
‭b)‬ ‭The admin monitors compliance with relevant data protection regulations and can perform‬
‭audits as needed.‬
‭
15)‬ ‭As a system admin,
I want to manage and resolve any customer profile issues (e.g., data‬
‭discrepancies, security concerns) so that the platform remains reliable and trustworthy.‬
‭a)‬ ‭The admin dashboard includes tools for identifying and resolving issues related to‬
‭customer profiles.‬
‭b)‬ ‭The system logs all changes and access to customer profiles for audit purposes.‬
‭
16)‬ ‭As a customer,
I want to receive suggestions for new services or promotions based on my‬
‭booking history so that I can discover relevant offers.‬
‭a)‬ ‭The system analyzes booking history and suggests relevant services or promotions.‬
‭b)‬ ‭Suggestions are displayed in the customer’s profile or sent via preferred communication‬
‭methods.‬
```

## **‭Feature 5: Vendor Profiles: Manage business info and services.‬‬‬**
```
‭1)‬ ‭As a vendor,
I want to create a profile for my business, including basic information such as‬
‭name, address, and contact details, so that customers can find and book my services.‬
‭a)‬ ‭The vendor can enter business details like name, address, phone number, and email.‬
‭b)‬ ‭The system stores and displays this information on the vendor's public profile page.‬
‭
2)‬ ‭As a vendor,
I want to upload a logo and images of my business so that my profile looks‬
‭professional and attractive to potential customers.‬
‭a)‬ ‭The vendor can upload a logo and multiple images.‬
‭b)‬ ‭The images are displayed prominently on the vendor's profile.‬
‭
3)‬ ‭As a vendor,
I want to list and manage the services I offer, including descriptions, prices, and‬
‭durations, so that customers know exactly what I provide.‬
‭a)‬ ‭The vendor can create and edit service listings, including service name, description, price,‬
‭and duration.‬
‭b)‬ ‭Changes to services are updated in real-time and reflected on the vendor's profile.‬
‭
4)‬ ‭As a vendor,
I want to categorize my services into different types (e.g., hair care, massage,‬
‭skincare) so that customers can easily navigate through my offerings.‬
‭a)‬ ‭The vendor can assign categories to each service.‬
‭b)‬ ‭Services are displayed in categorized sections on the vendor's profile.‬
‭
5)‬ ‭As a vendor,
I want to manage my business hours and available appointment slots so that‬
‭customers can only book when I am open and available.‬
‭a)‬ ‭The vendor can set business hours and define available time slots.‬
‭b)‬ ‭The system only shows these time slots to customers during the booking process.‬
‭
6)‬ ‭As a vendor,
I want to update my profile information, such as changing my address or contact‬
‭details, so that my profile remains accurate and up to date.‬
‭a)‬ ‭The vendor can edit any part of their profile information at any time.‬
‭b)‬ ‭Updates are reflected immediately on the public profile.‬
‭‬
‭7)‬ ‭As a vendor, I want to view and respond to customer reviews and ratings so that I can engage‬
‭with customers and address any feedback.‬
‭a)‬ ‭The vendor can see all customer reviews and ratings on their profile.‬
‭b)‬ ‭The vendor has the option to respond to reviews publicly or privately.‬

‭8)‬ ‭As a vendor,
I want to set up and manage promotions or discounts for my services so that I can‬
‭attract more customers during specific periods.‬
‭a)‬ ‭The vendor can create promotions with specific start and end dates.‬
‭b)‬ ‭The system applies these promotions during booking, and customers are notified of the‬
‭discounts.‬

‭9)‬ ‭As a vendor,
I want to track my booking statistics and view reports on customer engagement so‬
‭that I can analyze my business performance.‬
‭a)‬ ‭The vendor dashboard includes analytics on bookings, customer demographics, and‬
‭revenue.‬
‭b)‬ ‭Reports can be generated and downloaded for specific date ranges.‬
‭
10)‬ ‭As a vendor,
I want to manage staff profiles, including assigning services they can perform‬
‭and their availability, so that I can efficiently manage my team.‬
‭a)‬ ‭The vendor can create staff profiles and assign specific services to each staff member.‬
‭b)‬ ‭The vendor can also set and manage each staff member's availability.‬
‭
11)‬‭As a vendor,
I want to receive notifications about new bookings, cancellations, or customer‬
‭inquiries so that I can respond quickly and manage my schedule effectively.‬
‭a)‬ ‭The system sends real-time notifications via email or SMS for all relevant activities.‬
‭b)‬ ‭Notifications include all necessary details such as customer information, service booked,‬
‭and time.‬
‭
12)‬ ‭As a vendor,
I want to manage my subscription plan and payment details for using the‬
‭platform so that I can ensure my account remains active.‬
‭a)‬ ‭The vendor can view current subscription details, upgrade or downgrade their plan, and‬
‭manage payment methods.‬
‭b)‬ ‭The system provides reminders for upcoming payments and processes payments‬
‭automatically if configured.‬
‭
13)‬ ‭As a vendor,
I want to integrate my profile with third-party services like social media or‬
‭Google My Business so that I can increase my online presence.‬
‭a)‬ ‭The vendor can link their profile to social media accounts or Google My Business.‬
‭b)‬ ‭The system syncs relevant information and updates across these platforms.‬
‭
14)‬ ‭As a vendor,
I want to deactivate or delete my profile if I decide to stop using the platform so‬
‭that my business is no longer visible to customers.‬
‭a)‬ ‭The vendor can deactivate or delete their profile from the settings.‬
‭b)‬ ‭The system confirms the action and removes the profile from public view.‬
‭
15)‬ ‭As a vendor,
I want to see a list of my repeat customers and their booking history so that I‬
‭can offer personalized services and loyalty rewards.‬
‭a)‬ ‭The vendor dashboard includes a list of repeat customers with their booking history.‬
‭b)‬ ‭The vendor can use this information to offer personalized promotions or loyalty rewards.‬

‭16)‬ ‭As a vendor,
I want to export my customer and booking data so that I can use it for offline‬
‭analysis or integration with other systems.‬
‭a)‬ ‭The vendor can export data in common formats (e.g., CSV, Excel) from the dashboard.‬
‭b)‬ ‭The exported data includes customer details, booking history, and payment information.‬
‭
17)‬ ‭As a system admin,
I want to manage vendor profiles and provide support in case of issues‬
‭so that vendors have a seamless experience on the platform.‬
‭a)‬ ‭The admin dashboard includes tools for managing and assisting vendor profiles.‬
‭b)‬ ‭The system logs all support interactions for future reference.‬
```


## **‭‭‭Feature 6: Staff: Schedule and track employee work.‬‬‬**
```
‭1)‬ ‭As a vendor,
I want to create staff profiles with personal information (name, contact details, job‬
‭role) so that I can manage my team effectively.‬
‭i)‬ ‭The vendor can create a profile for each staff member, including their name, contact‬
‭details, and job role.‬
‭ii)‬ ‭The staff profiles are stored securely and can be updated as needed.‬
‭
2)‬ ‭As a vendor,
I want to assign specific services to each staff member based on their skills and‬
‭expertise so that customers can book with the appropriate staff.‬
‭i)‬ ‭The vendor can assign or update the services that each staff member is qualified to‬
‭perform.‬
‭ii)‬ ‭The system ensures that only the assigned services are available for customers to‬
‭book with that staff member.‬
‭
3)‬ ‭As a vendor,
I want to set and manage each staff member’s work schedule, including their‬
‭availability and time off, so that customers can book appointments accordingly.‬
‭i)‬ ‭The vendor can set up a weekly or monthly work schedule for each staff member,‬
‭including start and end times.‬
‭ii)‬ ‭The system updates availability in real-time, reflecting any time off or changes in the‬
‭schedule.‬
‭
4)‬ ‭As a vendor,
I want to view and manage staff appointments so that I can monitor their workload‬
‭and ensure efficient operations.‬
‭i)‬ ‭The vendor can view a calendar showing all appointments assigned to each staff‬
‭member.‬
‭ii)‬ ‭The vendor can reschedule, reassign, or cancel appointments as needed.‬
‭
5)‬ ‭As a vendor,
I want to receive notifications about staff schedules, such as when a staff member‬
‭is overbooked or unavailable, so that I can take appropriate action.‬
‭i)‬ ‭The system alerts the vendor if a staff member is overbooked or has conflicting‬
‭appointments.‬
‭ii)‬ ‭Notifications include details on the conflict and options for resolving it.‬

‭6)‬ ‭As a vendor,
I want to track staff performance metrics, such as the number of appointments‬
‭completed and customer satisfaction ratings, so that I can evaluate their performance.‬
‭i)‬ ‭The vendor dashboard includes performance metrics for each staff member,‬
‭including completed appointments and average customer ratings.‬
‭ii)‬ ‭The vendor can generate reports on staff performance over specific periods.‬
‭
7)‬ ‭As a vendor,
I want to assign different levels of access to staff profiles so that each employee‬
‭has access to only the information they need to perform their job.‬
‭i)‬ ‭The vendor can set access permissions for each staff profile, determining what‬
‭information and tools they can access.‬
‭ii)‬ ‭Staff members only see information relevant to their role, such as their schedule‬
‭and assigned appointments.‬
‭
8)‬ ‭As a vendor,
I want to track staff attendance, including check-in and check-out times, so that I‬
‭can monitor punctuality and manage payroll.‬
‭i)‬ ‭The system includes a feature for staff to check in and check out of their shifts.‬
‭ii)‬ ‭The vendor can view attendance records and use them for payroll processing.‬
‭
9)‬ ‭As a vendor,
I want to allow staff members to manage their own schedules, such as requesting‬
‭time off or swapping shifts, so that they can have flexibility while ensuring coverage.‬
‭i)‬ ‭Staff members can request time off or swap shifts with other staff members through‬
‭the system.‬
‭ii)‬ ‭The vendor receives these requests and can approve or deny them, with the‬
‭system updating the schedule accordingly.‬
‭
10)‬ ‭As a vendor,
I want to communicate directly with staff members through the platform (e.g.,‬
‭send messages or alerts) so that I can coordinate easily and keep everyone informed.‬
‭i)‬ ‭The system includes a messaging feature that allows the vendor to send individual‬
‭or group messages to staff.‬
‭ii)‬ ‭Messages can include alerts, schedule changes, or general announcements.‬
‭
11)‬ ‭As a staff member,
I want to view my upcoming schedule and appointments so that I can‬
‭prepare for my workday.‬
‭i)‬ ‭Staff members have access to their schedules and can view upcoming‬
‭appointments and tasks.‬
‭ii)‬ ‭The schedule is updated in real-time, reflecting any changes made by the vendor or‬
‭other staff members.‬
‭
12)‬ ‭As a staff member,
I want to receive notifications about my upcoming appointments,‬
‭schedule changes, or messages from the vendor so that I am always up to date.‬
‭i)‬ ‭The system sends real-time notifications to staff members regarding their schedule,‬
‭upcoming appointments, or messages from the vendor.‬
‭ii)‬ ‭Notifications can be received via email, SMS, or in-app alerts.‬

‭13)‬ ‭As a staff member,
I want to leave notes or feedback on appointments I’ve completed so that‬
‭the vendor and other staff can see how the service went.‬
‭i)‬ ‭Staff members can add notes or feedback to appointments after they are‬
‭completed.‬
‭ii)‬These notes are visible to the vendor and relevant staff and can be used to improve‬
‭service or follow up with customers.‬

14)‬ ‭As a vendor,
I want to manage payroll based on staff attendance and completed‬
‭appointments so that I can ensure accurate and timely payment.‬
‭i)‬ ‭The vendor can access payroll features that calculate payments based on hours‬
‭worked and appointments completed.‬
‭ii)‬ ‭The system generates payroll reports and allows the vendor to process payments‬
‭directly through the platform.‬
‭
15)‬ ‭As a system admin,
I want to ensure that staff profiles and schedules are secure and that‬
‭access is controlled to protect sensitive information.‬
‭i)‬ ‭The system enforces security measures such as role-based access control for staff‬
‭profiles.‬
‭ii)‬ ‭The admin can monitor and audit staff access and activity to ensure compliance‬
‭with security policies.‬
‭
16)‬ ‭As a vendor,
I want to assign specific tasks or responsibilities to staff members (e.g.,‬
‭inventory management, customer follow-up) so that they can contribute to overall business‬
‭operations.‬
‭i)‬ ‭The vendor can assign tasks to staff members through their profiles.‬
‭ii)‬ ‭The system tracks task completion and provides reminders to staff for pending‬
‭tasks.‬

```




























