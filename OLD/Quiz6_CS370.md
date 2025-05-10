QUIZ NUMBER: 6
CLASS: CS-370


================================================================================
QUESTION 1:
Select the three “AAA”s of access control?

[x] Authorization

[x] Accounting

[x] Authentication

[ ] Auditing


================================================================================
QUESTION 2:
Which of the following is user authentication? (pick all that apply)

[ ] Granting users access

[ ] Verifying something is genuine

[x] Verifying someone is who they claim to be

[x] Establishing identity


================================================================================
QUESTION 3:
Which of the following is multi-factor authentication? (pick one)

[ ] User authenticating to the server using multiple passwords

[ ] User authenticating to the server and server authenticating to the user

[ ] Server authenticating to the user

[x] User authenticating to an ATM using a chip card and PIN


================================================================================
QUESTION 4:
In which of the following access control models, do regular users get to adjust the access policy?

[ ] Mandatory Access Control

[ ] Role-based Access Control

[x] Discretionary Access Control

[ ] Attribute-based Access Control


================================================================================
QUESTION 5:
In which of the following access control models, are attributes of the environment used for access control?

[x] Attribute-based Access Control

[ ] Role-based Access Control

[ ] Discretionary Access Control

[ ] Mandatory Access Control


================================================================================
QUESTION 6:
Which of the following are factors of authentication? (pick all that apply)

[x] What you know

[x] What you do

[x] Where you are

[x] What you have

[x] Who you are


================================================================================
QUESTION 7:
Which of the following statements accurately describe complementation information in MFA?

[ ] Allows multiple factors to rely on the exact same secret, thereby simplifying management.

[x] Combines distinct types of factors to cover multiple vulnerabilities.

[x] Helps ensure that if one factor is compromised, the attacker still needs another factor.

[ ] Replaces weaker factors with multiple instances of the same factor to create redundancy.


================================================================================
QUESTION 8:
In which of the following access control models, do labels associated with processes and resources determine allowed access?

[ ] Discretionary Access Control

[x] Mandatory Access Control

[ ] Role-based Access Control

[ ] Attribute-based Access Control


================================================================================
QUESTION 9:
Which factors best illustrate how complementation information protects against a stolen password?

[x] A dedicated hardware token generating a one-time code.

[ ] A unique PIN that is identical to the password.

[x] An SMS-based verification code sent to the user’s phone.

[ ] A second password stored on the same password manager.

[x] A fingerprint scan on a separate reader device.


================================================================================
QUESTION 10:
Which of the following are key principles of access control? (select all that apply)

[ ] Least common mechanism

[x] Least privilege

[x] Separation-of-duty

[ ] Open system


================================================================================
QUESTION 11:
Which of the following is obtained by slicing the access control matrix by columns?

[x] Access Control Lists

[ ] Column

[ ] Capabilities

[ ] Mandatory Access Control


================================================================================
QUESTION 12:
Which of the following are true about password-based systems? (pick all that apply)

[x] Less expensive as no special hardware is needed

[x] Easy to implement

[x] Easier to replace or recover from lost passwords


================================================================================
QUESTION 13:
Which of the following is true about Anderson’s formula? (pick all that apply)

[x] Only provides an upper bound of strength

[ ] Doesn’t take into account attacker’s computational ability

[x] Assumes uniform distribution on user picked passwords

[x] Assumes a targeted attack


================================================================================
QUESTION 14:
Which of the following is obtained by slicing the access control matrix by rows?

[ ] Role-based access control

[ ] Mandatory Access Control

[x] Capabilities

[ ] Access Control Lists


================================================================================
QUESTION 15:
Which of the following password strategies provides passwords with higher entropy and are easier to remember?

[x] Passphrases

[ ] System generated passwords with special characters


================================================================================
QUESTION 16:
Which of the following access review is easier when using access control lists?

[ ] Per-subject review

[ ] Per-access-right review

[x] Per-object review


================================================================================
QUESTION 17:
How are passwords stored on a login server?

[x] One-way hash functions of the passwords are stored so that a server compromise does not leak passwords

[ ] None of the above

[ ] Stored as plaintext so the server can compare the user supplied password with that stored in the file during authentication

[ ] Stored as encrypted ciphertext so that a server compromise does not leak user passwords


================================================================================
QUESTION 18:
Which of the following access review is easier when using capabilities?

[ ] Per-access-right review

[x] Per-subject review

[ ] Per-object review


================================================================================
QUESTION 19:
Which of the following statements about Bloom Filters used for proactive password checking are TRUE? (pick all that apply)

[ ] Bloom filter will never label a good password (i.e., not in bad password list) as a bad password

[x] Bloom filter will always catch a bad password (i.e., password in the bad list)

[ ] Bloom filter may sometimes miss a bad password

[x] Bloom filter may sometimes falsely label a good password (i.e., not in bad password list) as a bad password


================================================================================
QUESTION 20:
Can S2 remove seek permission on disk D1 from S1?

[x] Yes, because of R3

[ ] No

![Image](/courses/1999695/files/111334969/preview)


================================================================================
QUESTION 21:
Looking at the access matrix above and using the rules governing access matrix change, can S1 grant Read access on F1 to S3?

[x] No

[ ] Yes, because of R2

![Image](/courses/1999695/files/111334969/preview)


================================================================================
QUESTION 22:
Looking at the access matrix above and using the rules governing access matrix change, can S3 remove wakeup permission on process P1 from S1?

[x] No

[ ] Yes, because of R5

![Image](/courses/1999695/files/111334969/preview)


================================================================================
QUESTION 23:
Which of the following is a type-1 dictionary attack?

[ ] An attacker attempts to log into to a bank account by repeatedly guessing the password

[x] An attacker gains access to the password file on a server and repeatedly guesses passwords to find a match


================================================================================
QUESTION 24:
In Unix File System Access Control, superuser is exempt from usual access control restrictions and has system wide-access. Is this statement true or false?

[x] True

[ ] False


================================================================================
QUESTION 25:
What is the downside of re-using a password across multiple sites?

[ ] Re-using passwords results in loss of accountability

[x] Re-using passwords increases impact of compromise as one compromised site could impact other unrelated sites that use the same passwords

[ ] Re-using strong passwords has no downsides as they are hard to crack and reduces the effort on part of the user


================================================================================
QUESTION 26:
Which of the following capture the intuition for integrity levels? (select all that apply)

[ ] The higher the integrity level associated with an object or file the higher the confidence that no can read the information

[ ] The higher the integrity level associated with an object or file the more confidential the information contained within it is

[x] The higher the integrity level associated with an object or file the higher the confidence in reliability of the information contained within it

[x] The higher the integrity level associated with an object or file the higher the confidence that it will execute correctly


================================================================================
QUESTION 27:
Why might a second factor based on a separate device be considered more complementary than a second factor on the same device?

[x] An attacker controlling the primary device might intercept both factors if they are on that single device

[x] Storing the factors separately makes it harder to compromise them simultaneously.

[x] A separate device factor forces the attacker to physically steal two items instead of one.

[ ] Using one device for all factors simplifies user experience and thus is generally preferred.


================================================================================
QUESTION 28:
Which of the following is the simple security property in BIBA integrity model?

[ ] No write down

[x] No write up

[ ] No read down

[ ] No read up


================================================================================
QUESTION 29:
Which of the following is the *-security (star security) property BIBA integrity model?

[x] No read down

[ ] No write down

[ ] No write up

[ ] No read up


================================================================================
QUESTION 30:
Authentication is a critical first step for_________.

[ ] Auditing

[ ] Encryption

[x] Authorization

[ ] Identification


================================================================================
QUESTION 31:
When using a Bloom filter, an item can be either ‘definitely not’ in the set or ______ in the set.

[ ] Certainly

[ ] Likely

[ ] Yes

[x] Possiblly


================================================================================
QUESTION 32:
Consider the following two integrity labels:Label 1: (Medium: {p1, p2})Label 2: (Low: {p1, p2}).Here Low and Medium are integrity levels with Low < Medium and p1, p2 and p3 are categories.Which of the following statements is true?

[ ] Label 2 dominates Label 1

[ ] Neither label dominates the other

[x] Label 1 dominates Label 2

[ ] None of the above


================================================================================
QUESTION 33:
A ______ table is a pre-computed list of password hashes attackers use to speed up cracking.

[ ] Bloom

[x] Rainbow

[ ] Master

[ ] Lookup


================================================================================
QUESTION 34:
Which of the following is true about Chinese Wall Model? (select all that apply)

[ ] Chinese Wall model is an Integrity model like BIBA

[ ] None of these

[ ] Chinese Wall model is a Confidentiality model like BLP

[x] Chinese Wall model enforces conflict of interest policies


================================================================================
QUESTION 35:
Which of the following is the simple security property in Chinese Wall model?

[ ] None of these

[ ] Cannot read two object belonging to different CI classes

[ ] Cannot read two objects belonging to the same data set (DS)

[x] Cannot read two objects belonging to the same CI class but in separate data sets (DSes)


================================================================================
QUESTION 36:
Which of the following are implications of *-security (star security) property in Chinese Wall model? (select all that apply)

[x] To write to an object O the subject must first have read access to it

[ ] None of these

[x] Cannot write to objects belonging to different data sets (DSes)

[x] Can write to an object O if only if all the objects the subject has ever read are in the same DS (data set) as O


================================================================================
QUESTION 37:
Which of the following is the simple security property in BLP confidentiality model?

[ ] No write up

[ ] No write down

[x] No read up

[ ] No read down


================================================================================
QUESTION 38:
Which of the following is the *-security (star security) property in BLP confidentiality model?

[ ] No write up

[ ] No read down

[x] No write down

[ ] No read up


================================================================================
QUESTION 39:
When using DAC along with MAC, i.e., DAC in MAC), Which of the following is true? (Select one or more)

[x] Only grant access if both MAC and DAC allow access.

[ ] If MAC policy allows the requested access then grant access

[x] Only grant access if MAC policy also grants access

[ ] If DAC policy allows the requested access then grant access


================================================================================
QUESTION 40:
Consider the following two security labels:Label 1: (Restricted: {p1, p2})Label 2: (Secret: {p1, p3}).Here Restricted and Secret are security levels with Restricted < Secret and p1, p2 and p3 are categories.Using the BLP confidentiality model, which of the following statements is true? (Select one)

[ ] None of the above

[ ] Label 2 dominates Label 1

[x] Neither label dominates the other

[ ] Label 1 dominates Label 2


================================================================================
QUESTION 41:
Which of the following is NOT True about Roles in RBAC?

[x] Role is a group of Users

[ ] Permissions can be revoked from a role

[ ] Role-permission associations are relatively stable

[ ] Role is defined by a set of permissions


================================================================================
QUESTION 42:
Which of the following are True about RBAC? (select all that apply)

[x] Roles represent job functions, competency or authority in an organization

[x] A Role can have multiple Users assigned to it

[x] A User can have multiple Role assigned to her

[x] In RBAC, Roles are mapped to permissions and, and Users are mapped to Roles


================================================================================
QUESTION 43:
Which of the following is NOT TRUE about RBAC Sessions?

[ ] A session can have multiple active users in it

[x] A user can activate multiple roles in a session


================================================================================
QUESTION 44:
Consider a hierarchical Role-Based Access Control (RBAC) system where a role Manager inherits from a role Clerk. A Manager is permitted to perform operations Review and Approve on resource Report, and a Clerk is permitted to perform operation Edit on resource Report. User Alice is assigned to role Manager, and user Bob is assigned to role Clerk.TRUE/FALSE: Bob is necessarily also assigned to the role Manager.

[ ] True

[x] False


================================================================================
QUESTION 45:
Consider a hierarchical Role-Based Access Control (RBAC) system where a role Manager inherits from a role Clerk. A Manager is permitted to perform operations Review and Approve on resource Report, and a Clerk is permitted to perform operation Edit on resource Report. User Alice is assigned to role Manager, and user Bob is assigned to role Clerk.TRUE/FALSE: Alice necessarily has privileges to Edit.

[x] True

[ ] False


================================================================================
QUESTION 46:
Which of the following are TRUE about Static Separation of Duty (SSoD) and Dynamic Separation of Duty (DSoD)? (select all that apply)

[x] SSoD is applied during role assignment where as DSoD is applied during role activation in sessions

[x] DSoD is like SSoD but is used to deal with temporal conflicts of interest

[x] Both prevent conflicts of interest

[ ] Neither can support mutually exclusive roles


================================================================================
QUESTION 47:
Which of the following Security Principle does RBAC support? (select all that apply)

[x] Least-privilege

[ ] Open Design

[ ] Least Common Mechanism

[x] Separation of Privilege

[ ] Economy of Mechanism


================================================================================
QUESTION 48:
Who is responsible for establishing access permissions MAC access control model?

[ ] .The owner of the resource

[ ] The user requiring access to the resource

[ ] The system administrator and the owner of the resource

[x] The system administrator
