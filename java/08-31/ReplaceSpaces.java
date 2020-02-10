class ReplaceSpaces
{
    public static void main(String args[])
    {
        // bruteForce("Mr John Smith", 13);
        backwards(" Mr John");
    }

    public static void bruteForce(String str)
    {
        int spaceCount = 0;
        int length = str.length();
        char [] charArray = str.toCharArray();
        for (char c : charArray)
        {
            if (c == ' ')
            {
                spaceCount++;
            }
            int finalLength = length + spaceCount * 2;
            // have to copy array into a larger array of length finalLength
            char [] finalCharArray = new char [finalLength + 2];
            for (int i = 0; i < charArray.length; i++)
            {
                finalCharArray[i] = charArray[i];
            }

            for (int idx = 0; idx < finalLength; idx++)
            {
                if(finalCharArray[idx] == ' ')
                {
                    for (int i = idx + 1; i < finalLength; i++)
                    {
                        finalCharArray[i + 2] = finalCharArray[i];
                    }
                    finalCharArray[idx] = '%';
                    finalCharArray[idx + 1] = '2';
                    finalCharArray[idx + 2] = '0';
                }
            }

            System.out.println(String.valueOf(finalCharArray));
        }

    }
    public static void backwards(String str)
    {
        int spaceCount = 0;
        int length = str.length();
        char [] charArray = str.toCharArray();
        for (char c : charArray)
        {
            if (c == ' ')
            {
                spaceCount++;
            }
        }

        int finalLength = length + spaceCount * 2;

        char [] finalCharArray = new char [finalLength];
        // for (int i = 0; i < charArray.length; i++)
        // {
        //     finalCharArray[i] = charArray[i];
        // }

        int destIdx = finalLength - 1;
        for(int idx = length - 1; idx >= 0; idx--)
        // int changingLength = finalLength;
        {
            if (charArray[idx] == ' ')
            {
                finalCharArray[destIdx] = '0';
                finalCharArray[destIdx - 1] = '2';
                finalCharArray[destIdx - 2] = '%';
                destIdx -= 3;
                System.out.println(destIdx);
            }
            else
            {
              finalCharArray[destIdx] = charArray[idx];
              destIdx--;
            }
        }

        System.out.println(String.valueOf(finalCharArray));

    }
}
