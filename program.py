from experta import *

class StudentFacts(Fact):
    pass


class CareerExpertSystem(KnowledgeEngine):

    @Rule(StudentFacts(likes='Maths'),
          StudentFacts(likes='Physics'))
    def mechanical(self):
        print("\nSuggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Programming'),
          StudentFacts(likes='Maths'))
    def computer(self):
        print("\nSuggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Biology'),
          StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("\nSuggested Career Path: Biotechnology")

    @Rule(StudentFacts(likes='Circuits'),
          StudentFacts(likes='Maths'))
    def electronics(self):
        print("\nSuggested Career Path: Electronics Engineering")

    @Rule(StudentFacts(likes='Biology'),
          StudentFacts(likes='Medicine'))
    def doctor(self):
        print("\nSuggested Career Path: Doctor / Medical Science")

    @Rule(StudentFacts(likes='Accounts'),
          StudentFacts(likes='Economics'))
    def commerce(self):
        print("\nSuggested Career Path: Chartered Accountant (CA)")

    @Rule(StudentFacts(likes='Drawing'),
          StudentFacts(likes='Creativity'))
    def architecture(self):
        print("\nSuggested Career Path: Architecture")

    @Rule(StudentFacts(likes='Programming'),
          StudentFacts(likes='AI'))
    def ai_engineer(self):
        print("\nSuggested Career Path: Artificial Intelligence Engineer")

    @Rule(StudentFacts(likes='Chemistry'),
          StudentFacts(likes='Physics'))
    def chemical(self):
        print("\nSuggested Career Path: Chemical Engineering")


def main():
    engine = CareerExpertSystem()
    engine.reset()

    print("====================================")
    print("     CAREER PATH EXPERT SYSTEM")
    print("====================================")

    print("\nAvailable Interests:")
    print("1. Maths")
    print("2. Physics")
    print("3. Chemistry")
    print("4. Biology")
    print("5. Programming")
    print("6. Circuits")
    print("7. Medicine")
    print("8. Accounts")
    print("9. Economics")
    print("10. Drawing")
    print("11. Creativity")
    print("12. AI")

    interests = input(
        "\nEnter your interests separated by commas: "
    ).split(',')

    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))

    print("\nCareer Suggestion:")
    engine.run()


if __name__ == "__main__":
    main()
