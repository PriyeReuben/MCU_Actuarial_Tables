class Sex:

    def __init__(self, name):
        self.name = name

    def get_sex(self):
        import gender_guesser.detector as gender

        d = gender.Detector()
        returned_gender = str(d.get_gender(str(self.name)))
        if returned_gender == 'male':
            return 'male'
        elif returned_gender == 'mostly_male':
            return 'male'
        elif returned_gender == 'unknown':
            return 'male'
        elif returned_gender == 'female':
            return 'female'
        elif returned_gender == 'mostly_female':
            return 'female'
        else:
            return 'male'