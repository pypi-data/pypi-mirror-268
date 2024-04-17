from dataclasses import dataclass
from typing import ClassVar, List
from datetime import datetime, date, time

@dataclass
class Organization:
    organization_id: int
    name: str

    @classmethod
    def from_json(cls, data):
        return cls(
            organization_id=data['OrganizationId'],
            name=data['Name']
        )

@dataclass
class WeightClass:
    weight_class_id: int
    catch_weight: str
    weight: str
    description: str
    abbreviation: str

    @classmethod
    def from_json(cls, data):
        return cls(
            weight_class_id=data['WeightClassId'],
            catch_weight=data.get('CatchWeight', None),
            weight=data.get('Weight', None),
            description=data['Description'],
            abbreviation=data['Abbreviation']
        )

@dataclass
class Referee:
    referee_id: int
    first_name: str
    last_name: str

    @classmethod
    def from_json(cls, data):
        return cls(
            referee_id=data['RefereeId'],
            first_name=data['FirstName'],
            last_name=data['LastName']
        )

@dataclass
class RuleSet:
    possible_rounds: int
    description: str

    @classmethod
    def from_json(cls, data):
        return cls(
            possible_rounds=data['PossibleRounds'],
            description=data['Description']
        )

@dataclass
class FighterScore:
    fighter_id: int
    score: int

    @classmethod
    def from_json(cls, data):
        return cls(
            fighter_id=data['FighterId'],
            score=data['Score']
        )

@dataclass
class Judge:
    judge_id: int
    first_name: str
    last_name: str
    fighters: List[FighterScore]

    @classmethod
    def from_json(cls, data):
        fighters = [FighterScore.from_json(fighter) for fighter in data['Fighters']]
        return cls(
            judge_id=data['JudgeId'],
            first_name=data['JudgeFirstName'],
            last_name=data['JudgeLastName'],
            fighters=fighters
        )

@dataclass
class FightScore:
    judge: Judge

    @classmethod
    def from_json(cls, data):
        judge = Judge.from_json(data)
        return cls(judge=judge)

@dataclass
class Result:
    method: str
    ending_round: int
    ending_time: time
    ending_strike: str
    ending_target: str
    ending_position: str
    ending_submission: str
    ending_notes: str
    fight_of_the_night: bool
    fight_scores: List[FightScore]

    @classmethod
    def from_json(cls, data):
        fight_scores = [FightScore.from_json(score) for score in data['FightScores']]
        #example ending time: "5:00"
        ending_time = datetime.strptime(data['EndingTime'], "%M:%S").time()
        return cls(
            method=data['Method'],
            ending_round=data['EndingRound'],
            ending_time=ending_time,
            ending_strike=data['EndingStrike'],
            ending_target=data['EndingTarget'],
            ending_position=data['EndingPosition'],
            ending_submission=data['EndingSubmission'],
            ending_notes=data['EndingNotes'],
            fight_of_the_night=data['FightOfTheNight'],
            fight_scores=fight_scores
        )

@dataclass
class Name:
    first: str
    last: str
    nick: str

    @classmethod
    def from_json(cls, data):
        return cls(
            first=data['FirstName'],
            last=data['LastName'],
            nick=data['NickName']
        )

@dataclass
class Location:
    city: str
    state: str
    country: str
    tri_code: str

    @classmethod
    def from_json(cls, data):
        return cls(
            city=data['City'],
            state=data['State'],
            country=data['Country'],
            tri_code=data['TriCode']
        )

@dataclass
class Record:
    wins: int
    losses: int
    draws: int
    no_contests: int

    @classmethod
    def from_json(cls, data):
        return cls(
            wins=data['Wins'],
            losses=data['Losses'],
            draws=data['Draws'],
            no_contests=data['NoContests']
        )

@dataclass
class FighterWeight:
    weight_class_id: int
    weight_class_order: int
    description: str
    abbreviation: str

    @classmethod
    def from_json(cls, data):
        return cls(
            weight_class_id=data['WeightClassId'],
            weight_class_order=data['WeightClassOrder'],
            description=data['Description'],
            abbreviation=data['Abbreviation']
        )

@dataclass
class Outcome:
    outcome_id: int
    outcome: str

    @classmethod
    def from_json(cls, data):
        return cls(
            outcome_id=data['OutcomeId'],
            outcome=data['Outcome']
        )

@dataclass
class Fighter:
    fighter_id: int
    mma_id: int
    name: Name
    born: Location
    fighting_out_of: Location
    record: Record
    dob: str
    age: int
    stance: str
    weight: float
    height: float
    reach: float
    ufc_link: str
    weight_classes: List[FighterWeight]
    corner: str
    weigh_in: float
    outcome: Outcome
    ko_of_the_night: bool
    submission_of_the_night: bool
    performance_of_the_night: bool

    def __repr__(self):
        return f'<Fighter {self.name.first} {self.name.last}, {self.fighter_id}>'

    @classmethod
    def from_json(cls, data):
        name = Name.from_json(data['Name'])
        born = Location.from_json(data['Born'])
        fighting_out_of = Location.from_json(data['FightingOutOf'])
        record = Record.from_json(data['Record'])
        weight_classes = [WeightClass.from_json(wc) for wc in data['WeightClasses']]
        outcome = Outcome.from_json(data['Outcome'])
        return cls(
            fighter_id=data['FighterId'],
            mma_id=data['MMAId'],
            name=name,
            born=born,
            fighting_out_of=fighting_out_of,
            record=record,
            dob=data['DOB'],
            age=data['Age'],
            stance=data['Stance'],
            weight=data['Weight'],
            height=data['Height'],
            reach=data['Reach'],
            ufc_link=data['UFCLink'],
            weight_classes=weight_classes,
            corner=data['Corner'],
            weigh_in=data['WeighIn'],
            outcome=outcome,
            ko_of_the_night=data['KOOfTheNight'],
            submission_of_the_night=data['SubmissionOfTheNight'],
            performance_of_the_night=data['PerformanceOfTheNight']
        )

@dataclass
class Tracking:
    action_id: int
    fighter_id: int
    type_: str
    round_number: int
    round_time: str
    timestamp: datetime

    @classmethod
    def from_json(cls, data):
        timestamp = datetime.strptime(data['Timestamp'], "%Y-%m-%dT%H:%M:%SZ")
        return cls(
            action_id=data['ActionId'],
            fighter_id=data['FighterId'],
            type_=data['Type'],
            round_number=data['RoundNumber'],
            round_time=data['RoundTime'],
            timestamp=timestamp
        )

@dataclass
class Fight:
    fight_id: int
    fight_order: int
    status: str
    card_segment: str
    card_segment_start_time: datetime
    card_segment_broadcaster: str
    fighters: List[Fighter]
    result: Result
    weight_class: WeightClass
    accolades: List[str]
    referee: Referee
    rule_set: RuleSet
    fight_night_tracking: List[Tracking]

    def __repr__(self):
        fighters_str = " vs. ".join([f"{fighter.name.first} {fighter.name.last}" for fighter in self.fighters])
        return f'<Fight "{fighters_str}", {self.card_segment_start_time}, {self.fight_id}>'

    @classmethod
    def from_json(cls, data):
        fighters = [Fighter.from_json(fighter) for fighter in data['Fighters']]
        result = Result.from_json(data['Result'])
        weight_class = WeightClass.from_json(data['WeightClass'])
        referee = Referee.from_json(data['Referee'])
        rule_set = RuleSet.from_json(data['RuleSet'])
        fight_night_tracking = [Tracking.from_json(tracking) for tracking in data['FightNightTracking']]
        start_time = datetime.strptime(data['CardSegmentStartTime'], "%Y-%m-%dT%H:%MZ")
        return cls(
            fight_id=data['FightId'],
            fight_order=data['FightOrder'],
            status=data['Status'],
            card_segment=data['CardSegment'],
            card_segment_start_time=start_time,
            card_segment_broadcaster=data['CardSegmentBroadcaster'],
            fighters=fighters,
            result=result,
            weight_class=weight_class,
            accolades=data['Accolades'],
            referee=referee,
            rule_set=rule_set,
            fight_night_tracking=fight_night_tracking
        )

@dataclass
class Event:
    id: int
    name: str
    start_time: datetime
    timezone: str
    status: str
    live_event_id: int
    live_fight_id: int
    live_round_number: int
    live_round_elapsed_time: str
    organization: Organization
    location: Location
    fight_card: List[Fight]

    def __repr__(self):
        date_str = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
        return f'<Event "{self.name}", {date_str}, {self.id}>'

    def get_main_event(self):
        return self.fight_card[0]
        
    @classmethod
    def from_json(cls, data):
        data = data['LiveEventDetail']
        organization = Organization.from_json(data['Organization'])
        location = Location.from_json(data['Location'])
        fight_card = [Fight.from_json(card) for card in data['FightCard']]
        start_time = datetime.strptime(data['StartTime'], "%Y-%m-%dT%H:%MZ")
        return cls(
            id=data['EventId'],
            name=data['Name'],
            start_time=start_time,
            timezone=data['TimeZone'],
            status=data['Status'],
            live_event_id=data['LiveEventId'],
            live_fight_id=data['LiveFightId'],
            live_round_number=data['LiveRoundNumber'],
            live_round_elapsed_time=data['LiveRoundElapsedTime'],
            organization=organization,
            location=location,
            fight_card=fight_card
        )
