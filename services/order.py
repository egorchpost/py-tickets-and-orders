from datetime import datetime

from db.models import Order, Ticket, User


def create_order(
        tickets: dict,
        username: str,
        date: datetime | None = None
) -> Order:
    user = User.objects.get(username=username)

    order = Order.objects.create(
        user=user,
        created_at=date,
    )

    for ticket in tickets:
        Ticket.objects.create(
            row=ticket["row"],
            seat=ticket["seat"],
            movie_session_id=ticket["movie_session"],
            order=order,
        )

    return order
