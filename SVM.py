{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "from skimage import data, io, filters\n",
    "from skimage import io\n",
    "from skimage.color import rgb2gray\n",
    "from skimage.feature import hog \n",
    "from skimage.transform import resize\n",
    "import pickle\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import glob\n",
    "import random\n",
    "import csv\n",
    "import os \n",
    "from sklearn.ensemble import  RandomForestClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.svm import LinearSVC\n",
    "from sklearn.naive_bayes import MultinomialNB,GaussianNB\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.svm import SVC\n",
    "import json\n",
    "import time\n",
    "import gzip\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Rowida Nagah\\\\EEG\\\\user_3'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "R =os.path.dirname(os.path.realpath('__file__'))\n",
    "R"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>image</th>\n",
       "      <th>top_left_x</th>\n",
       "      <th>top_left_y</th>\n",
       "      <th>bottom_right_x</th>\n",
       "      <th>bottom_right_y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>user_3/A0.jpg</td>\n",
       "      <td>124</td>\n",
       "      <td>18</td>\n",
       "      <td>214</td>\n",
       "      <td>108</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>user_3/A1.jpg</td>\n",
       "      <td>124</td>\n",
       "      <td>18</td>\n",
       "      <td>214</td>\n",
       "      <td>108</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>user_3/A2.jpg</td>\n",
       "      <td>123</td>\n",
       "      <td>19</td>\n",
       "      <td>213</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>user_3/A3.jpg</td>\n",
       "      <td>122</td>\n",
       "      <td>21</td>\n",
       "      <td>212</td>\n",
       "      <td>111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>user_3/A4.jpg</td>\n",
       "      <td>122</td>\n",
       "      <td>20</td>\n",
       "      <td>212</td>\n",
       "      <td>110</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           image  top_left_x  top_left_y  bottom_right_x  bottom_right_y\n",
       "0  user_3/A0.jpg         124          18             214             108\n",
       "1  user_3/A1.jpg         124          18             214             108\n",
       "2  user_3/A2.jpg         123          19             213             109\n",
       "3  user_3/A3.jpg         122          21             212             111\n",
       "4  user_3/A4.jpg         122          20             212             110"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('user_3_loc.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ll= []\n",
    "for i in df.image :\n",
    "    if 'A' in i :\n",
    "        ll.append('A')\n",
    "    elif 'B' in i :\n",
    "        ll.append('B')\n",
    "    elif 'C' in i :\n",
    "        ll.append('C')\n",
    "    elif 'D' in i :\n",
    "        ll.append('D')\n",
    "    elif 'E' in i :\n",
    "        ll.append('E')\n",
    "    elif 'F' in i :\n",
    "        ll.append('F')\n",
    "    elif 'H' in i :\n",
    "        ll.append('H')\n",
    "    elif 'G' in i :\n",
    "        ll.append('G')\n",
    "    elif 'B' in i :\n",
    "        ll.append('B')\n",
    "    elif 'I' in i :\n",
    "        ll.append('I')\n",
    "    elif 'K' in i :\n",
    "        ll.append('K')\n",
    "    elif 'L' in i :\n",
    "        ll.append('L')\n",
    "    elif 'M' in i :\n",
    "        ll.append('M')\n",
    "    elif 'N' in i :\n",
    "        ll.append('N')\n",
    "    elif 'B' in i :\n",
    "        ll.append('B')\n",
    "    elif 'O' in i :\n",
    "        ll.append('O')\n",
    "    elif 'P' in i :\n",
    "        ll.append('P')\n",
    "    elif 'Q' in i :\n",
    "        ll.append('Q')\n",
    "    elif 'R' in i :\n",
    "        ll.append('R')\n",
    "    elif 'S' in i :\n",
    "        ll.append('S')\n",
    "    elif 'T' in i :\n",
    "        ll.append('T')\n",
    "    elif 'U' in i :\n",
    "        ll.append('U')\n",
    "    elif 'V' in i :\n",
    "        ll.append('V')\n",
    "    elif 'W' in i :\n",
    "        ll.append('W')\n",
    "    elif 'X' in i :\n",
    "        ll.append('X')\n",
    "    elif 'Y' in i :\n",
    "        ll.append('Y')\n",
    "    \n",
    "df_row['A-Z'] = ll \n",
    "\n",
    "df_row.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
