import ipih

from pih import A
from pih.collections import Result

from pih.collections import PolibasePerson
from NotificationAutomationService.api import NotificationApi as Api


class ReviewNotificationApi:
    @staticmethod
    def start_review_notification_distribution_action(test: bool = False) -> bool:
        sender_profile: A.CT_ME_WH_W.Profiles = A.CT_ME_WH_W.Profiles.MARKETER
        if A.S_P_RN.is_on() or test:
            if A.C_ME_WH_W.accessibility(sender_profile):

                def every_action(person: PolibasePerson, inpatient: bool) -> None:
                    telephone_number: str | None = A.D_F.telephone_number_international(
                        person.telephoneNumber
                    )
                    # polibase format telephone number 7
                    if A.C.telephone_number_international(telephone_number):
                        if A.ME_WH_W_Q.add(
                            A.S_P_RN.notification_text(
                                person,
                                Api.check_for_notification_confirmation(
                                    telephone_number, sender_profile.value, test
                                ),
                            ),
                            telephone_number,
                            sender_profile,
                        ):
                            A.E.send(
                                A.CT_E.POLIBASE_PERSON_REVIEW_NOTIFICATION_WAS_REGISTERED,
                                (person.pin, inpatient, 2),
                            )

                def map_function(pin_list: list[int]) -> list[PolibasePerson]:
                    return (A.R_P.persons_by_pin(pin_list) or Result(data=[])).data

                for inpatient in [True, False]:
                    A.R.every(
                        lambda person: every_action(person, inpatient),
                        A.R.map(
                            map_function,
                            A.R_P.persons_pin_by_visit_date(
                                A.D.today(-A.S_P_RN.day_delta(), as_datetime=True),
                                inpatient=inpatient,
                                test=test,
                            ),
                            False,
                        ),
                    )
                return True
            else:
                return False
        else:
            return False
