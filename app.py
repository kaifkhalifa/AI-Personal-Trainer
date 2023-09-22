from flask import Flask, render_template, request

app = Flask(__name__)

# Define a class to represent Nutrition Articles
class NutritionArticle:
    def __init__(self, title, description, image_url, link):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.link = link

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    supplement_images = [
        'https://shop.lifetime.life/media/catalog/product/8/5/850009173034-rxsugar-swealthy-stix-30-stick-carton-q42022-2000x2000-front.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=700&width=700&canvas=700:700',
        'https://shop.lifetime.life/media/catalog/product/8/5/850009173140-rxsugar-organic-hazelnut-syrup-q42021-2000x2000-front.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=700&width=700&canvas=700:700',
        'https://shop.lifetime.life/media/catalog/product/b/l/bluechocalmond.png?quality=80&bg-color=255,255,255&fit=bounds&height=700&width=700&canvas=700:700',
    ]

    if request.method == 'POST':
        # Get selected goals and activities from the form
        selected_goals = request.form.getlist('goals')
        selected_activities = request.form.getlist('activities')

        # Implement your recommendation logic here based on selected goals and activities
        # You can use these selections to determine what to recommend
        recommendations = []

        # Define recommendation categories based on goals and activities
        recommendation_categories = {
            ('lose_weight', 'group_fitness'): ['Weight Loss', 'Group Fitness'],
            ('improve_health', 'yoga_meditation'): ['Health Improvement', 'Yoga & Meditation'],
            # Add more mappings based on your categories
        }

        # Check if there's a matching category for the selected goals and activities
        for category, category_recommendations in recommendation_categories.items():
            if all(goal in selected_goals and activity in selected_activities for goal, activity in category):
                recommendations.extend(category_recommendations)

        # If no specific category matches, provide some default recommendations
        if not recommendations:
            recommendations = [
                'ALPHA Strength Class',
                'Yoga and Meditation',
                # Add more default recommendations as needed
            ]

        # Define nutrition articles here (replace with actual data)
        nutrition_articles = [
            NutritionArticle(
                title='5 Moves You Will See in ROOT Yoga',
                description='A Life Time instructor breaks down a few of the foundational movements in this slower-paced yoga practice.',
                image_url='https://experiencelife.lifetime.life/wp-content/uploads/2023/09/MicrosoftTeams-image-47.jpg',
                link='https://experiencelife.lifetime.life/article/5-moves-youll-see-in-root-yoga/'
            ),
            NutritionArticle(
                title='Article 2',
                description='This is another interesting article about nutrition.',
                image_url='https://example.com/path-to-article-2-image.jpg',  # Replace with the actual image URL
                link='url_to_article_2'
            ),
            # Add more articles as needed
        ]

        # You can now pass the recommendations and nutrition_articles to your template
        return render_template('result.html', recommendations=recommendations, supplement_images=supplement_images, nutrition_articles=nutrition_articles)

    return render_template('result.html', supplement_images=supplement_images)

if __name__ == '__main__':
    app.run(debug=True)


