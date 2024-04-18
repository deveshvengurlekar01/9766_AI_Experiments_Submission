# Devesh Vengurlekar
# Roll No: 9766
# TE Comps A

class ExpertSystem:
    def __init__(self):
        self.rules = {
            "low_calorie": "Focus on consuming fruits, vegetables, lean proteins, and whole grains. Limit added sugars and fats.",
            "high_protein": "Include plenty of protein-rich foods such as lean meats, fish, eggs, dairy, legumes, and nuts.",
            "low_carb": "Limit carbohydrate intake and focus on consuming non-starchy vegetables, lean proteins, and healthy fats.",
            "balanced_diet": "Eat a variety of foods from all food groups, including fruits, vegetables, grains, protein-rich foods, and healthy fats."
        }

    def consult(self, dietary_needs):
        recommendations = []
        for need in dietary_needs:
            if need in self.rules:
                recommendations.append(self.rules[need])
            else:
                recommendations.append("Sorry, I'm not sure what to advise for '{}' dietary need.".format(need))
        return recommendations


def main():
    expert_system = ExpertSystem()
    # Example consultations
    print("Dietary needs: balanced_diet")
    print(expert_system.consult(["balanced_diet"]))
    print("\nDietary needs: high_protein, low_carb")
    print(expert_system.consult(["high_protein", "low_carb"]))
    print("\nDietary needs: low_protein")
    print(expert_system.consult(["low_protein"]))


if __name__ == "__main__":
    main()
