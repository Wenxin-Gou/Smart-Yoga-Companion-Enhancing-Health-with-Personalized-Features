#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
from tkinter import messagebox
from session_record import SessionRecord
from api_connector import APIConnector


class YogaSession:
    def __init__(self):
        self.api_connector = APIConnector()
        self.session_records = []
        self.mood_index = defaultdict(list)

    def start_session(self, mood, duration):
        try:
            music = self.api_connector.get_music_for_mood(mood)
            aroma = self.api_connector.get_aroma_for_mood(mood)
            light = self.api_connector.get_light_for_mood(mood)  
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            record = SessionRecord(timestamp, mood, music, aroma, duration)
            self.session_records.append(record)
            self.mood_index[mood].append(record)
            return music, aroma, light 
        except Exception as e:
            raise ValueError(f"Error starting session: {str(e)}")

    def save_records(self):
        try:
            with open("yoga_sessions.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:  # Write header only if the file is empty
                    writer.writerow(["Timestamp", "Mood", "Music", "Aroma", "Duration"])
                for record in self.session_records:
                    writer.writerow([record.timestamp, record.mood, record.music, record.aroma, record.duration])
        except IOError as e:
            messagebox.showerror("File Error", f"Failed to save records: {str(e)}")

    def plot_statistics(self):
        try:
            if not self.session_records:
                raise ValueError("No session records available for plotting.")
            
            self.session_records.sort(key=lambda x: x.timestamp)  # Timsort
            timestamps = [record.timestamp.split(" ")[0] for record in self.session_records]
            durations = [record.duration for record in self.session_records]

            plt.figure(figsize=(10, 6))
            plt.bar(timestamps, durations, color="skyblue")
            plt.xlabel("Date")
            plt.ylabel("Duration (minutes)")
            plt.title("Yoga Session Durations Over Time")
            plt.xticks(rotation=45, fontsize=8)
            plt.tight_layout()
            plt.show()
        except ValueError as ve:
            messagebox.showerror("Data Error", f"Error: {ve}")
        except Exception as e:
            messagebox.showerror("Plotting Error", f"Unexpected error: {str(e)}")

    def search_sessions_by_mood(self, mood):
        return self.mood_index.get(mood, [])

