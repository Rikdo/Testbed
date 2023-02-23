SELECT *, count(person_id) as numb
from facebook_event_checkin
join person on person.id = facebook_event_checkin.person_id
where event_name = "SQL Symphony Concert" and date between 20171201 and 20171233
group by person_id
having numb = 3