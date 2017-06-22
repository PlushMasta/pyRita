# -*- coding: utf8 -*-

import os
import fnmatch
from random import randint


class ShieldUp:
    rita01 = """// SaintRita Code Shield
// O powerful St. Rita, rightly called Saint of the Impossible,
// I come to you with confidence in my great need.
// You know well my trials, for you yourself were many times
// burdened in this life. Come to my help, speak for me, pray
// with me, intercede on my behalf before the Father. I know that
// God has a most generous heart and that he is a most loving Father.
// Join your prayers to mine and obtain for me the grace I desire (here mention your request).
// You who were so very pleasing to God on earth and are so much so now in heaven,
// I promise to use this favor, when granted, to better my life, to proclaim God's mercy,
// and to make you more widely known and loved. Amen.
"""
    rita02 = """// SaintRita Code Shield
// Dear Saint Rita, during your entire life on earth you found your happiness
// by following the will of our heavenly Father. Help me to be as trusting of
// God in all his designs for me., Help me this day to give myself to him as
// you did, without limit, without fear, without counting the cost. Help me to
// be generous in serving the needs of others, patient in all difficulties, forgiving
// toward all who injure me. Help me to learn more deeply the great mystery of the
// cross of Jesus, so that by embracing it as you did, I may come to experience its
// power to heal and to save. Amen
"""

    rita03 = """// SaintRita Code Shield
// Lord you are close to the brokenhearted; you save those whose spirit is crushed.
// Give us courage and strength in time of suffering so that like Saint Rita who
// shared in your Son's passion, we may enter more deeply into the mystery of suffering
// and experience the joy of redemption that lies at its heart. Amen
"""

    rita04 = """// SaintRita Code Shield
// God of mercy and peace you gave to Saint Rita the grace to love even those who live
// by hatred and revenge. As you, so graciously blessed her, I ask you to bless my family.
// Through the intercession of Saint Rita, model of patience and fortitude, bless and protect
// us from all selfish ways. Make us grow strong in the Spirit of Charity and forgiveness,
// and like your servant Rita, may we be faithful peacemakers in our family in our neighborhood,
// and in our world. Amen
"""
    prayers = []

    def __init__(self, dir_path):
        print("Kyrie eleison!")
        self.prayers = [self.rita01, self.rita02, self.rita03, self.rita04]
        file_list = self.cs_files(dir_path)
        if len(file_list) > 0:
            for f in file_list:
                self.strengthen_file(f)
        else:
            print("Nothing left to pray for.")

    def select_random_prayers(self):
        return self.prayers[randint(0, len(self.prayers) - 1)]

    def cs_files(self, directory):
        matches = []
        for root, dir_names, file_names in os.walk(directory):
            for filename in fnmatch.filter(file_names, '*.cs'):
                matches.append(os.path.join(root, filename))
        return matches

    def strengthen_file(self, file_path):
        file = open(file_path, "r")
        old_file = file.readlines()
        file.close()

        if len(old_file) > 0:
            if str(old_file[0]) != "// SaintRita Code Shield\n":
                new_file = open(file_path, "w")
                new_file.write(self.select_random_prayers() + "\n")
                new_file.writelines(old_file)
                new_file.close()
                print("+ %s Amen!" % file.name)
            else:
                print("- %s Is already shielded!" % file.name)
