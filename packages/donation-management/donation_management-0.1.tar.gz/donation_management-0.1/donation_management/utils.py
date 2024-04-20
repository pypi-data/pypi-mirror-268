import csv
from decimal import Decimal
from django.db.models import Sum
from .models import Donation

def get_total_donations():
    """Calculate total donations received."""
    total_donations = Donation.objects.aggregate(total=Sum('amount'))['total']
    return total_donations or Decimal(0)

def get_average_donation():
    """Calculate average donation amount."""
    total_donations = get_total_donations()
    donation_count = Donation.objects.count()
    if donation_count > 0:
        return total_donations / donation_count
    return Decimal(0)

def export_donations_to_csv(file_path):
    """Export donation data to a CSV file."""
    donations = Donation.objects.all()
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Donor', 'Amount', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for donation in donations:
            writer.writerow({'Donor': donation.donor.name, 'Amount': donation.amount, 'Date': donation.date})
