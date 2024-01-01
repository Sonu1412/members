import streamlit as st
import csv

def csv_to_list(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data_list.append(row)
    return data_list


def filter_and_categorize(csv_file_path, user_input1, user_input2):
    user_input1 = user_input1.replace(" ", "")  # Removing spaces from user input
    user_input2 = user_input2.replace(" ", "")

    both_present_data = []
    only_input1_data = []
    only_input2_data = []

    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Skip the header

        for row in csv_reader:
            row_cleaned = [cell.replace('nan', '') for cell in row]  # Remove 'nan' from cells
            row_lower = [col.lower().replace(" ", "") for col in row_cleaned]  # Removing spaces from CSV data

            if 'nan' not in row_lower and user_input1 in row_lower[1] and user_input2 in row_lower[1]:
                both_present_data.append(row_cleaned)
            elif 'nan' not in row_lower and user_input1 in row_lower[1]:
                only_input1_data.append(row_cleaned)
            elif 'nan' not in row_lower and user_input2 in row_lower[1]:
                only_input2_data.append(row_cleaned)

    return both_present_data, only_input1_data, only_input2_data

def main():
    st.title('CSV Data Filter Web App')

    csv_file_path = 'new2.csv'

    user_input1 = st.text_input('Enter First Name:')
    user_input2 = st.text_input('Enter Father Name:')
    user_input1 = user_input1.lower()
    user_input2 = user_input2.lower()

    if st.button('Filter Data'):
        both_present, only_input1, only_input2 = filter_and_categorize(csv_file_path, user_input1, user_input2)

        st.write(f"Data for '{user_input1}' and '{user_input2}':")
        
        st.write("\nBoth Inputs Present:")
        if both_present:
            displayed_both_present = [row[:5] + row[7:] for row in both_present]  # Excluding columns 5 and 6
            st.table(displayed_both_present)
        else:
            st.write("No data found.")

        st.write("\nOnly First Input Present:")
        if only_input1:
            displayed_only_input1 = [row[:5] + row[7:] for row in only_input1]  # Excluding columns 5 and 6
            st.table(displayed_only_input1)
        else:
            st.write("No data found.")

        st.write("\nOnly Second Input Present:")
        if only_input2:
            displayed_only_input2 = [row[:5] + row[7:] for row in only_input2]  # Excluding columns 5 and 6
            st.table(displayed_only_input2)
        else:
            st.write("No data found.")

if __name__ == '__main__':
    main()
