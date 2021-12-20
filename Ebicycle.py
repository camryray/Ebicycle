import streamlit as st
class Bicycle:
 
    def run(self, distance):
        self.distance = distance
        st.slider("用腳騎行了{} KM".format(self.distance))
     
class Ebicycle(Bicycle):
    def __init__(self,vol):
        self.vol = vol      #default electric quantity
        st.slider("當前電量：{}".format(self.vol))
    def fill_charge(self,fill_vol):
        self.vol += fill_vol    # charge electric
        st.slider("充電後電量：{}度".format(self.vol))
    def run(self,distance):
         st.slider("行駛前電量：{}".format(self.vol))
         e_distance = self.vol * 10
         if distance <= e_distance:
            self.vol = self.vol - distance/10
            st.slider("電動騎行{}km".format(distance))
            st.slider("電動車剩餘電量：{}".format(self.vol))
         else:
            st.slider("電動騎行{}km".format(e_distance))
            self.vol = 0
            super().run(distance-e_distance)
            st.slider("行駛後電量：{}".format(self.vol)
