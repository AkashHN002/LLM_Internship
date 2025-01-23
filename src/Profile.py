import MySQLdb
import random
import streamlit as st

db = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    database = 'mydemo'      
)

cursor = db.cursor()

activities = {
        'amenities': ['pool', 'spa', 'gym', 'tennis_court', 'business_center'],
        'dining': ['main_restaurant', 'cafe', 'bar', 'room_service', 'buffet'],
        'activities': ['city_tour', 'beach_activity', 'cooking_class', 'yoga', 'golf']
}

st.title("Profile Management")
user_id = st.text_input("Enter user Id ")
submit = st.button('Submit')
exist = cursor.execute("SELECT * FROM interaction WHERE User_id = %s", (user_id,))
if user_id:
    if exist:
        for i, act in enumerate(activities.keys()):
            st.write(f"{i+1} --> {act}")
        c = st.text_input("Choose the Category visited: ")
        if c:
            c = int(c)
            cat = list(activities.keys())[c-1]
            for i in range(len(activities[cat])):
                st.write(f"{i+1}--> {activities[cat][i]} ")
            
            n = st.text_input(f"""Choose any Preferances:  """)
            if n:
                n = int(n)
                pref = activities[cat][n-1]
                rating = st.text_input("Privide the rating for activity (0-5): ")
                time_spent = random.randint(30, 180)
                if rating:
                    rating = int(rating)
                    cursor.execute("INSERT INTO interaction VALUES(%s, %s, %s, %s, %s)", (user_id, cat, pref, rating, time_spent))
                    if cursor.rowcount:
                        db.commit()
                        st.write("Data Updated")
                        st.write(f"Choosed Category {cat}\nChoosed Activity {pref}")

    else:
        st.write("Data Not Found\nPlease give the following details: ")
        for i, act in enumerate(activities.keys()):
            st.write(f"{i+1} --> {act}")
        c = st.text_input("Choose the Category visited: ")
        if c:
            c = int(c)
            cat = list(activities.keys())[c-1]
            for i in range(len(activities[cat])):
                st.write(f"{i+1}--> {activities[cat][i]} ")
            
            n = st.text_input(f"""Choose any Preferances:  """)
            if n:
                n = int(n)
                pref = activities[cat][n-1]
                rating = st.text_input("Privide the rating for activity (0-5): ")
                time_spent = random.randint(30, 180)
                if rating:
                    rating = int(rating)
                    cursor.execute("INSERT INTO interaction VALUES(%s, %s, %s, %s, %s)", (user_id, cat, pref, rating, time_spent))
                    if cursor.rowcount:
                        db.commit()
                        st.write("Data Stored")