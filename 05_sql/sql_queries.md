BANK LOAN REPORT QUERY DOCUMENT
A.	BANK LOAN REPORT | SUMMARY
    KPI’s:
      Total Loan Applications
      SELECT COUNT(id) AS Total_Applications FROM bank_loan_data
      Total Applications: 38,576
      
      MTD Loan Applications
      SELECT COUNT(id) AS Total_Applications FROM bank_loan_data
      WHERE MONTH(issue_date) = 12
      MTD Loan Applications: 4,314
      
      PMTD Loan Applications
      SELECT COUNT(id) AS Total_Applications FROM bank_loan_data
      WHERE MONTH(issue_date) = 11
      PMTD Loan Applications: 4,035
      
      
      Total Funded Amount
      SELECT SUM(loan_amount) AS Total_Funded_Amount FROM bank_loan_data
       
      Total Funded Amount: 435757075
    
    MTD Total Funded Amount
    SELECT SUM(loan_amount) AS Total_Funded_Amount FROM bank_loan_data
    WHERE MONTH(issue_date) = 12
    MTD Total Funded Amount: 53981425
    
    PMTD Total Funded Amount
    SELECT SUM(loan_amount) AS Total_Funded_Amount FROM bank_loan_data
    WHERE MONTH(issue_date) = 11
    PMTD Total Funded Amount: 47754825
    
    
    Total Amount Received
    SELECT SUM(total_payment) AS Total_Amount_Collected FROM bank_loan_data
    Total Amount Received: 473070933
    
    MTD Total Amount Received
    SELECT SUM(total_payment) AS Total_Amount_Collected FROM bank_loan_data
    WHERE MONTH(issue_date) = 12
    MTD Total Amount Received: 58074380
    
    PMTD Total Amount Received
    SELECT SUM(total_payment) AS Total_Amount_Collected FROM bank_loan_data
    WHERE MONTH(issue_date) = 11
    PMTD Total Amount Received: 50132030
    
    
    
    Average Interest Rate
    SELECT AVG(int_rate)*100 AS Avg_Int_Rate FROM bank_loan_data
    Average Interest Rate: 12.0488314172048
    
    MTD Average Interest
    SELECT AVG(int_rate)*100 AS MTD_Avg_Int_Rate FROM bank_loan_data
    WHERE MONTH(issue_date) = 12
    MTD Average Interest: 12.3560408676042
    
    PMTD Average Interest
    SELECT AVG(int_rate)*100 AS PMTD_Avg_Int_Rate FROM bank_loan_data
    WHERE MONTH(issue_date) = 11
     PMTD Average Interest: 11.9417175498261
    
    
    
    Avg DTI
    SELECT AVG(dti)*100 AS Avg_DTI FROM bank_loan_data
    Avg DTI: 13.3274331211432
    
    MTD Avg DTI
    SELECT AVG(dti)*100 AS MTD_Avg_DTI FROM bank_loan_data
    WHERE MONTH(issue_date) = 12
    MTD Avg DTI: 13.6655377880425
    
    PMTD Avg DTI
    SELECT AVG(dti)*100 AS PMTD_Avg_DTI FROM bank_loan_data
    WHERE MONTH(issue_date) = 11
    PMTD Avg DTI:  13.3027335836364



GOOD LOAN ISSUED
Good Loan Percentage

    SELECT
        (COUNT(CASE WHEN loan_status = 'Fully Paid' OR loan_status = 'Current' THEN id END) * 100.0) / 
    	COUNT(id) AS Good_Loan_Percentage
    FROM bank_loan_data
    Good Loan Percentage: 86.175342181667

Good Loan Applications

    SELECT COUNT(id) AS Good_Loan_Applications FROM bank_loan_data
    WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'
    Good Loan Applications: 33243

Good Loan Funded Amount

    SELECT SUM(loan_amount) AS Good_Loan_Funded_amount FROM bank_loan_data
    WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'
    Good Loan Funded Amount: 370224850



Good Loan Amount Received

    SELECT SUM(total_payment) AS Good_Loan_amount_received FROM bank_loan_data
    WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'
    Good Loan Amount Received: 435786170

BAD LOAN ISSUED

Bad Loan Percentage

    SELECT
        (COUNT(CASE WHEN loan_status = 'Charged Off' THEN id END) * 100.0) / 
    	COUNT(id) AS Bad_Loan_Percentage
    FROM bank_loan_data
     Bad Loan Percentage: 13.824657818332

Bad Loan Applications

    SELECT COUNT(id) AS Bad_Loan_Applications FROM bank_loan_data
    WHERE loan_status = 'Charged Off'
    Bad Loan Applications: 5333

Bad Loan Funded Amount
    
    SELECT SUM(loan_amount) AS Bad_Loan_Funded_amount FROM bank_loan_data
    WHERE loan_status = 'Charged Off'
    Bad_Loan_funded_amount: 65532225

Bad Loan Amount Received

    SELECT SUM(total_payment) AS Bad_Loan_amount_received FROM bank_loan_data
    WHERE loan_status = 'Charged Off'
    Bad_Loan_amount_received: 37284763
    

LOAN STATUS

	SELECT
        loan_status,
        COUNT(id) AS LoanCount,
        SUM(total_payment) AS Total_Amount_Received,
        SUM(loan_amount) AS Total_Funded_Amount,
        AVG(int_rate * 100) AS Interest_Rate,
        AVG(dti * 100) AS DTI
    FROM
        bank_loan_data
    GROUP BY
        loan_status
        
Loan Status 	 Loan Count 	 Total Amount Received 	 Total Funded Amount 	 Interest Rate (%) 	 DTI (%)
Fully Paid  	 32,145     	 411,586,256           	 351,358,350         	 11.64             	 13.17
Charged Off 	 5,333      	 37,284,763            	 65,532,225          	 13.88             	 14.00
Current     	 1,098      	 2,419,914             	 18,866,500          	 15.10             	 14.72

SELECT 
	loan_status, 
	SUM(total_payment) AS MTD_Total_Amount_Received, 
	SUM(loan_amount) AS MTD_Total_Funded_Amount 
FROM bank_loan_data
WHERE MONTH(issue_date) = 12 
GROUP BY loan_status

loan_status	  MTD_Total_Amount_Received	 MTD_Total_Funded_Amount
Fully Paid	  47,815,851	                 41,302,025
Charged Off	  5,324,211	                 8,732,775
Current	      4,934,318	                 3,946,625







B.	BANK LOAN REPORT | OVERVIEW

MONTH

    SELECT 
    	MONTH(issue_date) AS Month_Munber, 
    	DATENAME(MONTH, issue_date) AS Month_name, 
    	COUNT(id) AS Total_Loan_Applications,
    	SUM(loan_amount) AS Total_Funded_Amount,
    	SUM(total_payment) AS Total_Amount_Received
    FROM bank_loan_data
    GROUP BY MONTH(issue_date), DATENAME(MONTH, issue_date)
    ORDER BY MONTH(issue_date)


Month Number	Month Name	Total Loan Applications	Total Funded Amount	Total Amount Received
1	            January	    2,332	                   25,031,650	         27,578,836
2	            February	  2,279	                   24,647,825	         27,717,745
3	            March	      2,627	                   28,875,700	         32,264,400
4	            April	      2,755	                   29,800,800	         32,495,533
5	May	2,911	31,738,350	33,750,523
6	June	3,184	34,161,475	36,164,533
7	July	3,366	35,813,900	38,827,220
8	August	3,441	38,149,600	42,682,218
9	September	3,536	40,907,725	43,983,948
10	October	3,796	44,893,800	49,399,567
11	November	4,035	47,754,825	50,132,030
12	December	4,314	53,981,425	58,074,380









STATE
SELECT 
	address_state AS State, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_data
GROUP BY address_state
ORDER BY address_state

	STATE	TOTAL LOAN APPLICATIONS	TOTAL FUNDED AMOUNT	TOTAL AMOUNT RECEIVED
1	AK	78	1,031,800	1,108,570
2	AL	432	4,949,225	5,492,272
3	AR	236	2,529,700	2,777,875
4	AZ	833	9,206,000	10,041,986
5	CA	6,894	78,484,125	83,901,234
6	CO	770	8,976,000	9,845,810
7	CT	730	8,435,575	9,357,612
8	DC	214	2,652,350	2,921,854
9	DE	110	1,138,100	1,269,136
10	FL	2,773	30,046,125	31,601,905
11	GA	1,355	15,480,325	16,728,040
12	HI	170	1,850,525	2,080,184
13	IA	5	56,450	64,482
14	ID	6	59,750	65,329
15	IL	1,486	17,124,225	18,875,941
16	IN	9	86,225	85,521
17	KS	260	2,872,325	3,247,394
18	KY	320	3,504,100	3,792,530
19	LA	426	4,498,900	5,001,160
20	MA	1,310	15,051,000	16,676,279
21	MD	1,027	11,911,400	12,985,170
22	ME	3	9,200	10,808
23	MI	685	7,829,900	8,543,660
24	MN	592	6,302,600	6,750,746
25	MO	660	7,151,175	7,692,732
26	MS	19	139,125	149,342
27	MT	79	829,525	892,047
28	NC	759	8,787,575	9,534,813
29	NE	5	31,700	24,542
30	NH	161	1,917,900	2,101,386
31	NJ	1,822	21,657,475	23,425,159
32	NM	183	1,916,775	2,084,485
33	NV	482	5,307,375	5,451,443
34	NY	3,701	42,077,050	46,108,181
35	OH	1,188	12,991,375	14,330,148
36	OK	293	3,365,725	3,712,649
37	OR	436	4,720,150	4,966,903
38	PA	1,482	15,826,525	17,462,908
39	RI	196	1,883,025	2,001,774



TERM
SELECT 
	term AS Term, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_data
GROUP BY term
ORDER BY term
TERM (MONTHS)	TOTAL LOAN APPLICATIONS	TOTAL FUNDED AMOUNT	TOTAL AMOUNT RECEIVED
36	28237	273,041,225	294,709,458
60	10339	162715850	178361475

EMPLOYEE LENGTH
SELECT 
	emp_length AS Employee_Length, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_data
GROUP BY emp_length
ORDER BY emp_length
Employee Length	Total Loan Applications	Total Funded Amount	Total Amount Received
< 1 year	4,575	44,210,625	47,545,011
1 year	3,229	32,883,125	35,498,348
10+ years	8,870	116,115,950	125,871,616
2 years	4,382	44,967,975	49,206,961
3 years	4,088	43,937,850	47,551,832
4 years	3,428	37,600,375	40,964,850
5 years	3,273	36,973,625	40,397,571
6 years	2,228	25,612,650	27,908,658
7 years	1,772	20,811,725	22,584,136
8 years	1,476	17,558,950	19,025,777
9 years	1,255	15,084,225	16,516,173

PURPOSE
SELECT 
	purpose AS PURPOSE, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_data
GROUP BY purpose
ORDER BY purpose

PURPOSE	TOTAL LOAN APPLICATIONS	TOTAL FUNDED AMOUNT	TOTAL AMOUNT RECEIVED
CAR	1,497	10,223,575	11,324,914
CREDIT CARD	4,998	58,885,175	65,214,084
DEBT CONSOLIDATION	18,214	232,459,675	253,801,871
EDUCATIONAL	315	2,161,650	2,248,380
HOME IMPROVEMENT	2,876	33,350,775	36,380,930
HOUSE	366	4,824,925	5,185,538
MAJOR PURCHASE	2,110	17,251,600	18,676,927
MEDICAL	667	5,533,225	5,851,372
MOVING	559	3,748,125	3,999,899
OTHER	3,824	31,155,750	33,289,676
RENEWABLE ENERGY	94	845,750	898,931
SMALL BUSINESS	1,776	24,123,100	23,814,817
VACATION	352	1,967,950	2,116,738
WEDDING	928	9,225,800	10,266,856


HOME OWNERSHIP
SELECT 
	home_ownership AS Home_Ownership, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_data
GROUP BY home_ownership
ORDER BY home_ownership
HOME OWNERSHIP	TOTAL LOAN APPLICATIONS	TOTAL FUNDED AMOUNT	TOTAL AMOUNT RECEIVED
MORTGAGE	17,198	219,329,150	238,474,438
NONE	3	16,800	19,053
OTHER	98	1,044,975	1,025,257
OWN	2,838	29,597,675	31,729,129
RENT	18,439	185,768,475	201,823,056


Note: We have applied multiple Filters on all the dashboards. You can check the results for the filters as well by modifying the query and comparing the results.
For e.g
See the results when we hit the Grade A in the filters for dashboards.
SELECT 
	purpose AS PURPOSE, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_data
WHERE grade = 'A'
GROUP BY purpose
ORDER BY purpose
