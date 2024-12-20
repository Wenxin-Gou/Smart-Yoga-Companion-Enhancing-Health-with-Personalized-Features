#!/usr/bin/env python
# coding: utf-8

# In[1]:


class APIConnector:
    def get_light_for_mood(self, mood):
        light_settings = {
            "relax": {"color": "blue", "intensity": "low"},
            "energize": {"color": "red", "intensity": "high"},
            "focus": {"color": "white", "intensity": "medium"},
        }
        return light_settings.get(mood, {"color": "default", "intensity": "default"})

    def get_music_for_mood(self, mood):
        music_recommendations = {
            "relax": "Calm instrumental music",
            "energize": "Upbeat pop playlist",
            "focus": "Ambient study tunes",
        }
        return music_recommendations.get(mood, "Default music")

    def get_aroma_for_mood(self, mood):
        aroma_recommendations = {
            "relax": "Lavender",
            "energize": "Citrus",
            "focus": "Peppermint",
        }
        return aroma_recommendations.get(mood, "Default aroma")


# In[ ]:




