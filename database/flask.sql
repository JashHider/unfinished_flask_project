-- create database exam_management
-- use exam_management;

create table accounts(
	accountID int(60) primary key auto_increment,
    name varchar(255),
    email varchar(255),
    password varchar(255)
);

insert into accounts (name, email, password)
VALUES ("Johnny", "johnnyislearning23@gmail.com", "learningiscool!"), -- student
	   ("John", "snakeeater2004@yahoo.com", "l3sEnf@ntst3rr!bl3s"), -- teacher
       ("Meryl", "merylgearsolid@gmail.com", "140.15"), -- student
       ("David", "twinsnak3s@outlook.com", "f0xh0uN#"), -- student
       ("Eli", "liquidsnake1@outlook.com", "ph@nt0mp@!n"), -- teacher
       ("Miller", "therealmastermiller23@icloud.com", "p3@c3w@1k3r") -- teacher
;

create table teacher(
	TID int(60) PRIMARY KEY auto_increment,
    accountID int(60),
    FOREIGN KEY (accountID) REFERENCES accounts(accountID)
);
insert into teacher(accountID)
VALUES (2), (5), (6);

create table student(
	SID int(60) PRIMARY KEY auto_increment,
    accountID int(60),
    FOREIGN KEY (accountID) REFERENCES accounts(accountID)
); 
insert into student(accountID)
VALUES (1), (3), (4)
;

create table tests(
	TID int(60),
    testID int(60) PRIMARY KEY auto_increment,
    testName varchar(255),
    FOREIGN KEY (TID) REFERENCES teacher(TID)
);
insert into tests (TID, testName)
VALUES	(1, "Outdoors: Survival Test"),
		(1, "CQC: Overview"),
        (2, "Biology"),
        (2, "History"),
        (3, "Psychology"),
        (3, "Stealth")
;
create table testQuestions(
	testID int(60),
    testQuestion varchar(255),
    answer varchar(255),
    FOREIGN KEY (testID) REFERENCES tests(testID)
);
insert into testQuestions (testID, testQuestion, answer)
VALUES	
(1, "What is the most important factor in a survival situation?", "Having clean water"), 
(1, "What is the rule of threes in survival?", "You can survive three minutes without air, three hours without water, and three days without food"), 
(1, "What is an important skill to have in a survival situation?", "Being able to start a fire"),
(2, "What's the primary objective of CQC?", "To take down enemies quickly and efficiently in close proximity"), 
(2, "What's an important principle of CQC?", "Maintaining situational awareness"), 
(2, "Which of the following is a common technique used in CQC?", "Using hand-to-hand combat techniques"),
(3, "What is the function of the mitochondira in a cell?", "To produce energy"), 
(3, "What is the basic unit of life?", "A cell"),
(3, "What is the role of DNA in heredity?", "It encodes the genetic information that is passed down from parent to offspring"),
(4, "What was the main cause of World War I?", "The assassination of Archduke Franz Ferdinand of Austria-Hungary"), 
(4, "Which of the following was a significant event during the American Civil War?", "The Emancipation Proclamation"), 
(4, "Who was the first president of the U.S.?", "George Washington"),
(5, "What is the definition of psychology?", "The study of the mind and behavior"), 
(5, "What is the name of the theory that suggests behavior is influenced by unconscious thoughts and desires?", "Psychoanalytic theory"), 
(5, "Which part of the brain is responsible for regulating emotions and decision-making?", "Amygdala"), 
(6, "What is the definition of stealth?", "The ability to move without being detected"), 
(6, "What is an important factor in being stealthy?", "Moving slowly and deliberately"), 
(6, "What's an example of using cover to remain stealthy?", "Hiding behind a tree")
;

create table testAttempts(
	SID int(60),
    testID int(60),
    testQuestion varchar(255),
    answer varchar(255),
    FOREIGN KEY (testID) REFERENCES tests(testID),
    FOREIGN KEY (SID) REFERENCES student(SID)
);