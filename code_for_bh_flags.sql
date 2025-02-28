--drop table #WANG_MEMS;

CREATE VOLATILE TABLE #WANG_MEMS AS (
  SELECT
    ab.admission_date (DATE) AS admission_date,
    ab.member_dim_ck,
    ab.external_member_id,
    ab.plan_dim_ck,
    ab.member_curr_ck,
    ab.authorization_ck,
    ab.event_reason_dim_ck,
    ab.um_service_type_dim_ck,
    ab.admission_source_dim_ck,
    ab.attend_prov_aff_dim_ck,
    ab.diagnosis_type,
    p.plan_type,
    m.member_amisys_nbr,
    m.sex,
    m.edw_member_ck,
    m.mpi_id,
    e.pro_generic_product_desc,
    d.diag_code AS diag_code,
    d.diag_desc AS diag_desc

  FROM etl_access_own.ft_authorization AS ab

  JOIN etl_access_own.dim_plan AS p
    ON ab.plan_dim_ck = p.plan_dim_ck

  JOIN etl_access_own.dim_member_curr AS m
    ON ab.member_dim_ck = m.member_dim_ck

  LEFT JOIN etl_access_own.dim_member_elig_curr AS e
    ON ab.member_elig_curr_ck = e.member_eligibility_ck

  LEFT JOIN etl_access_own.dim_diagnosis AS d
    ON ab.rpt_primary_diag_dim_ck = d.diag_code_dim_ck

  WHERE admission_date BETWEEN '2021-01-01 00:00:00' AND '2023-04-01 00:00:00'
    AND external_member_id IS NOT NULL -- cannot join if either admission_date or member_id is null††
    AND admission_date IS NOT NULL -- since a visit is defined as a unique admit_date and member_id
    AND (p.state_code in ('EF','FL','EK','TX','WA','EW','OR','MO','NH','NV','NM','CA','WI',
      'MS','EM','EE','EA','KA','EV','XW','ET','IN','LA','GA','ER','AR', 'IL',' AZ', 'OH', 'NE')
           OR p.plan_dim_ck IN (41,62,68,82,83,108,127,109,130,132,213,44,69,45,51,126,107,105,110,106,
           104,203,202,201,204,205,76,102,1,101,103,73,21,2,26,125,12,15,20,61,32,115,49,59,23,14,50,55,
           117,146,124,128,54,118,22,10,27,60,37,70,122,112,228,223,114,123,138,140,136,5,121,16,57,143,
           144,145,209,210,211,212,226,39,119,75,40,4,137,74,46))
    AND left(auth_nbr, 2) NOT IN ('OP', 'OB')
)
WITH DATA
PRIMARY INDEX(authorization_ck)
ON COMMIT PRESERVE ROWS;


/********************************************************
Step 1. Creating volatile tables to hold all diagnosis
          related to the diagnosis flags business partners
          want to look at/flag for the member
********************************************************/

/*******************
PTSD Diagnosis
*******************/
CREATE VOLATILE TABLE #PTSD_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%PTSD%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Trauma Diagnosis
*******************/
CREATE VOLATILE TABLE #TRAUMA_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%TRAUMA%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Self Harm Diagnosis
*******************/
CREATE VOLATILE TABLE #SELF_HARM_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%SELF%HARM%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Schizo Diagnosis
*******************/
CREATE VOLATILE TABLE #SCHIZO_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%SCHIZO%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
OCD Diagnosis
*******************/
CREATE VOLATILE TABLE #OCD_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%OBSESSIVE%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;

/*******************
COVID-19 Diagnosis
*******************/
CREATE VOLATILE TABLE #COVID19_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%COVID-19%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Depression Diagnosis
*******************/
CREATE VOLATILE TABLE #DEPRESSION_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%DEPRESSION%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Anxiety Diagnosis
*******************/
CREATE VOLATILE TABLE #ANXIETY_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%ANXIETY%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Dementia Diagnosis
*******************/
CREATE VOLATILE TABLE #DEMENTIA_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%DEMENTIA%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Parkinsons Diagnosis
*******************/
CREATE VOLATILE TABLE #PARKINSONS_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%PARKINSONS%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Bipolar Diagnosis
*******************/
CREATE VOLATILE TABLE #BIPOLAR_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%BIPOLAR%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
Ideation Diagnosis
*******************/
CREATE VOLATILE TABLE #SUICIDEATION_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%SUICIDAL IDEATION%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;

/*******************
Previous Suicide Diagnosis
*******************/
CREATE VOLATILE TABLE #SUIC_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%SUICIDE%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;

/*******************
Previous Personality Disorder Diagnosis
*******************/
CREATE VOLATILE TABLE #PD_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%PERSONALITY DISORDER%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;

/*******************
Borderline Personality Disorder Diagnosis
*******************/
CREATE VOLATILE TABLE #BPD_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE '%BORDERLINE PERSONALITY DISORDER%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;

/*******************
Chronic Pain Diagnosis
*******************/
CREATE VOLATILE TABLE #CHRONIC_PAIN_DIAGS AS
(
SELECT
DIAG_CODE
,DIAG_DESC

  FROM ETL_ACCESS_OWN.DIM_DIAGNOSIS

WHERE DIAG_DESC LIKE 'CHRONIC%PAIN%'

--Grab only one description per diagnosis code
QUALIFY ROW_NUMBER() OVER(PARTITION BY DIAG_CODE ORDER BY DIAG_DESC ASC) = 1
)
WITH DATA
PRIMARY INDEX(DIAG_CODE)
ON COMMIT PRESERVE ROWS;


/*******************
BH Diagnosis flags
*******************/
CREATE VOLATILE TABLE #BH_CLAIMS AS
(
SELECT DISTINCT
SERV.PLAN_DIM_CK
,SERV.CLAIM_NBR
/*Logic from Population health team to defint BH Claims*/
,(CASE WHEN UPPER(DIAG_GROUP.MPC_DESC) LIKE '%PSYCHIATRY%' THEN 1
       WHEN UPPER(DIAG_GROUP.MPC_DESC) LIKE '%CHEMICAL_DEPENDENCY%' THEN 1
  ELSE 0
  END
  ) BH_FLAG

  /*Service line table - multiple lines per claim*/
	FROM ETL_ACCESS_OWN.FT_SERVICE_TRANSACTION SERV


    INNER JOIN ETL_ACCESS_OWN.DIM_MEMBER_CURR MEM
      ON SERV.MEMBER_CURR_CK = MEM.MEMBER_CURR_CK
      AND SERV.PLAN_DIM_CK = MEM.PLAN_DIM_CK

      /*Limit to our membership*/
        INNER JOIN (SELECT DISTINCT
                    MPI_ID

                        FROM #WANG_MEMS
                   ) T05
          ON MEM.MPI_ID = T05.MPI_ID

  /*Get diagnosis group to determine BH*/
      LEFT JOIN ETL_ACCESS_OWN.DIM_DIAGNOSIS_GROUPER DIAG_GROUP
          ON SERV.PRIMARY_DIAG_GROUPER_DIM_CK = DIAG_GROUP.DIAG_GROUPER_DIM_CK
)
WITH DATA
PRIMARY INDEX(PLAN_DIM_CK, CLAIM_NBR)
ON COMMIT PRESERVE ROWS;


/********************************************************
Step 2. Making a table with the claims with these
         specific diagnosis for the member's we're interested
         in and when these claims actually happened
********************************************************/

DROP TABLE MANDA_OWN_TABLES.PYR8S_BH_DATA_T01;

CREATE TABLE MANDA_OWN_TABLES.PYR8S_BH_DATA_T01 AS
(
SELECT
SERV.PLAN_DIM_CK
,SERV.MPI_ID
,SERV.SERV_DATE
,DIAG.CLAIM_NBR
,DIAG.DIAG_CODE
,(CASE WHEN DIAG.DIAG_CODE = PTSD.DIAG_CODE THEN 1 ELSE 0 END) PTSD
,(CASE WHEN DIAG.DIAG_CODE = TRAUMA.DIAG_CODE THEN 1 ELSE 0 END) TRAUMA
,(CASE WHEN DIAG.DIAG_CODE = SELF_HARM.DIAG_CODE THEN 1 ELSE 0 END) SELF_HARM
,(CASE WHEN DIAG.DIAG_CODE = SCHIZO.DIAG_CODE THEN 1 ELSE 0 END) SCHIZO
,(CASE WHEN DIAG.DIAG_CODE = OCD.DIAG_CODE THEN 1 ELSE 0 END) OCD
,(CASE WHEN DIAG.DIAG_CODE = COVID19.DIAG_CODE THEN 1 ELSE 0 END) COVID19
,(CASE WHEN DIAG.DIAG_CODE = DEPRESSION.DIAG_CODE THEN 1 ELSE 0 END) DEPRESSION
,(CASE WHEN DIAG.DIAG_CODE = ANXIETY.DIAG_CODE THEN 1 ELSE 0 END) ANXIETY
,(CASE WHEN DIAG.DIAG_CODE = DEMENTIA.DIAG_CODE THEN 1 ELSE 0 END) DEMENTIA
,(CASE WHEN DIAG.DIAG_CODE = PARKINSONS.DIAG_CODE THEN 1 ELSE 0 END) PARKINSONS
,(CASE WHEN DIAG.DIAG_CODE = BIPOLAR.DIAG_CODE THEN 1 ELSE 0 END) BIPOLAR
,(CASE WHEN DIAG.DIAG_CODE = SUICIDTN.DIAG_CODE THEN 1 ELSE 0 END) SUICIDTN
,(CASE WHEN DIAG.DIAG_CODE = SUIC.DIAG_CODE THEN 1 ELSE 0 END) SUICIDE
,(CASE WHEN DIAG.DIAG_CODE = PD.DIAG_CODE THEN 1 ELSE 0 END) PERS_DIS
,(CASE WHEN DIAG.DIAG_CODE = BPD.DIAG_CODE THEN 1 ELSE 0 END) BPD_DIS
,(CASE WHEN DIAG.DIAG_CODE = CP.DIAG_CODE THEN 1 ELSE 0 END) CHRON_PAIN
,BH.BH_FLAG BEHAVIORAL_HEALTH

  FROM ETL_ACCESS_OWN.BRG_CLAIM_DIAGNOSIS DIAG

    /*Grab date of claim and only pull claims for our members*/
    INNER JOIN (SELECT
                SERV.PLAN_DIM_CK
                ,T05.MPI_ID
                ,SERV.CLAIM_NBR
                ,MIN(SERV.SERVICE_START_DATE_DIM_CK) SERV_DATE

                  FROM ETL_ACCESS_OWN.FT_SERVICE_TRANSACTION SERV

                    INNER JOIN ETL_ACCESS_OWN.DIM_MEMBER_CURR MEM
                      ON SERV.MEMBER_CURR_CK = MEM.MEMBER_CURR_CK
                      AND SERV.PLAN_DIM_CK = MEM.PLAN_DIM_CK

                    /*Limit to our membership*/
                    INNER JOIN (SELECT DISTINCT
                              MPI_ID

                                    FROM #WANG_MEMS
                               ) T05
                      ON MEM.MPI_ID = T05.MPI_ID

                GROUP BY 1,2,3
                ) SERV
      ON DIAG.CLAIM_NBR = SERV.CLAIM_NBR


    /*Left join to each out our diagnosis tables to make flags*/
      LEFT JOIN #PTSD_DIAGS PTSD
        ON DIAG.DIAG_CODE = PTSD.DIAG_CODE

      LEFT JOIN #TRAUMA_DIAGS TRAUMA
         ON DIAG.DIAG_CODE = TRAUMA.DIAG_CODE

      LEFT JOIN #SELF_HARM_DIAGS SELF_HARM
        ON DIAG.DIAG_CODE = SELF_HARM.DIAG_CODE

      LEFT JOIN #SCHIZO_DIAGS SCHIZO
        ON DIAG.DIAG_CODE = SCHIZO.DIAG_CODE

      LEFT JOIN #OCD_DIAGS OCD
         ON DIAG.DIAG_CODE = OCD.DIAG_CODE

      LEFT JOIN #COVID19_DIAGS COVID19
         ON DIAG.DIAG_CODE = COVID19.DIAG_CODE

      LEFT JOIN #DEPRESSION_DIAGS DEPRESSION
         ON DIAG.DIAG_CODE = DEPRESSION.DIAG_CODE

      LEFT JOIN #ANXIETY_DIAGS ANXIETY
         ON DIAG.DIAG_CODE = ANXIETY.DIAG_CODE

      LEFT JOIN #DEMENTIA_DIAGS DEMENTIA
         ON DIAG.DIAG_CODE = DEMENTIA.DIAG_CODE

      LEFT JOIN #PARKINSONS_DIAGS PARKINSONS
         ON DIAG.DIAG_CODE = PARKINSONS.DIAG_CODE

      LEFT JOIN #BIPOLAR_DIAGS BIPOLAR
         ON DIAG.DIAG_CODE = BIPOLAR.DIAG_CODE

      LEFT JOIN #SUICIDEATION_DIAGS SUICIDTN
         ON DIAG.DIAG_CODE = SUICIDTN.DIAG_CODE

      LEFT JOIN #SUIC_DIAGS SUIC
         ON DIAG.DIAG_CODE = SUIC.DIAG_CODE

      LEFT JOIN #PD_DIAGS PD
         ON DIAG.DIAG_CODE = PD.DIAG_CODE

      LEFT JOIN #BPD_DIAGS BPD
         ON DIAG.DIAG_CODE = BPD.DIAG_CODE

      LEFT JOIN #CHRONIC_PAIN_DIAGS CP
         ON DIAG.DIAG_CODE = CP.DIAG_CODE

      LEFT JOIN #BH_CLAIMS BH
        ON DIAG.CLAIM_NBR = BH.CLAIM_NBR
        AND DIAG.PLAN_DIM_CK = BH.PLAN_DIM_CK

)
WITH DATA
PRIMARY INDEX(PLAN_DIM_CK, MPI_ID, CLAIM_NBR, SERV_DATE);


/********************************************************
Step 3. Looking at specific opioids the member has
          had within the past 30 days (prior to admission)
********************************************************/

/******************************************
Buprenorphine Prescription in last 30 days
******************************************/

CREATE VOLATILE TABLE #BUPRENORPHINE AS (
SELECT
T05.PLAN_DIM_CK
,T05.MPI_ID
,T05.admission_date
,Sum(CASE WHEN PHARMACY.AMT_PAID > 0 THEN 1
     ELSE 0
     END) AS BUPREN_CLAIMS


    FROM  ETL_ACCESS_OWN.FT_PHARMACY_CLAIM PHARMACY

      INNER JOIN ETL_ACCESS_OWN.DIM_DRUG DRUG
        ON PHARMACY.NATIONAL_DRUG_CODE_NBR = DRUG.NATIONAL_DRUG_CODE_NBR

      /*Convert fill date to actual date*/
      INNER JOIN ETL_ACCESS_OWN.DIM_DATE DD
        ON PHARMACY.FILL_DATE_DIM_CK = DD.DATE_DIM_CK

      INNER JOIN ETL_ACCESS_OWN.DIM_MEMBER_CURR MEM
        ON PHARMACY.PLAN_DIM_CK = MEM.PLAN_DIM_CK
        AND PHARMACY.PRESCRIBER_MEMBER_CURR_CK = MEM.MEMBER_CURR_CK

      /*join so we can make sure serv date is < admission date*/
      INNER JOIN #WANG_MEMS T05
        ON MEM.MPI_ID = T05.MPI_ID

/*Pull only number of claims for 30 days prior to admission date*/
WHERE 1=1
AND DD.DATE_DATE BETWEEN (T05.admission_date - 30) AND T05.admission_date
AND UPPER(DRUG.GPI_10_SEGMENT_DESC) LIKE '%BUPRENORPHINE%'

GROUP BY 1,2,3
)
WITH DATA
PRIMARY INDEX(PLAN_DIM_CK, MPI_ID, admission_date)
ON COMMIT PRESERVE ROWS;


/****************************************
Naloxone Prescription in last 30 days
*****************************************/
--DROP TABLE #NALOXONE;
CREATE VOLATILE TABLE #NALOXONE AS (
SELECT
PHARMACY.PLAN_DIM_CK
,T05.MPI_ID
,T05.admission_date
,Sum(CASE WHEN PHARMACY.AMT_PAID > 0 THEN 1
     ELSE 0
     END) AS NALOXONE_CLAIMS


    FROM  ETL_ACCESS_OWN.FT_PHARMACY_CLAIM PHARMACY

      INNER JOIN ETL_ACCESS_OWN.DIM_DRUG DRUG
        ON PHARMACY.NATIONAL_DRUG_CODE_NBR = DRUG.NATIONAL_DRUG_CODE_NBR

      /*Convert fill date to actual date*/
      INNER JOIN ETL_ACCESS_OWN.DIM_DATE DD
        ON PHARMACY.FILL_DATE_DIM_CK = DD.DATE_DIM_CK

      INNER JOIN ETL_ACCESS_OWN.DIM_MEMBER_CURR MEM
        ON PHARMACY.PLAN_DIM_CK = MEM.PLAN_DIM_CK
        AND PHARMACY.PRESCRIBER_MEMBER_CURR_CK = MEM.MEMBER_CURR_CK

      /*join so we can make sure serv date is < model run date*/
      INNER JOIN #WANG_MEMS T05
        ON MEM.MPI_ID = T05.MPI_ID

/*Pull only number of claims for 30 days prior to model run date*/
WHERE 1=1
AND DD.DATE_DATE BETWEEN (T05.admission_date - 30) AND T05.admission_date
AND UPPER(DRUG.GPI_10_SEGMENT_DESC) LIKE '%NALOXONE%'

GROUP BY 1,2,3
)
WITH DATA
PRIMARY INDEX(PLAN_DIM_CK, MPI_ID, admission_date)
ON COMMIT PRESERVE ROWS;

/***************************************************
Other type of Opioid Prescription in last 30 days
***************************************************/
--DROP TABLE #OPIOIDS;
CREATE VOLATILE TABLE #OPIOIDS AS (
SELECT
PHARMACY.PLAN_DIM_CK
,T05.MPI_ID
,T05.admission_date
,Sum(CASE WHEN PHARMACY.AMT_PAID > 0 THEN 1
     ELSE 0
     END) AS OPIOID_CLAIMS


    FROM  ETL_ACCESS_OWN.FT_PHARMACY_CLAIM PHARMACY

      INNER JOIN ETL_ACCESS_OWN.DIM_DRUG DRUG
        ON PHARMACY.NATIONAL_DRUG_CODE_NBR = DRUG.NATIONAL_DRUG_CODE_NBR

      /*Convert fill date to actual date*/
      INNER JOIN ETL_ACCESS_OWN.DIM_DATE DD
        ON PHARMACY.FILL_DATE_DIM_CK = DD.DATE_DIM_CK

      INNER JOIN ETL_ACCESS_OWN.DIM_MEMBER_CURR MEM
        ON PHARMACY.PLAN_DIM_CK = MEM.PLAN_DIM_CK
        AND PHARMACY.PRESCRIBER_MEMBER_CURR_CK = MEM.MEMBER_CURR_CK

      /*join so we can make sure serv date is < model run date*/
      INNER JOIN #WANG_MEMS T05
        ON MEM.MPI_ID = T05.MPI_ID

/*Pull only number of claims for 30 days prior to model run date*/
WHERE 1=1
AND DD.DATE_DATE BETWEEN (T05.admission_date - 30) AND T05.admission_date
AND (UPPER(DRUG.GPI_4_SEGMENT_DESC) LIKE '%OPIOID%'
        AND UPPER(DRUG.GPI_10_SEGMENT_DESC) NOT LIKE ('%BUPRENORPHINE%')
        AND UPPER(DRUG.GPI_10_SEGMENT_DESC) NOT LIKE ('%NALOXONE%')
        )

GROUP BY 1,2,3
)
WITH DATA
PRIMARY INDEX(PLAN_DIM_CK, MPI_ID, admission_date)
ON COMMIT PRESERVE ROWS;

/********************************************************
Step 4. Join this back to our original table, making sure
         to only count the diagnosis prior to our model
         run date
********************************************************/

DROP TABLE MANDA_OWN_TABLES.PYR8S_BH_DATA_T02;

CREATE TABLE MANDA_OWN_TABLES.PYR8S_BH_DATA_T02 AS
(
  SELECT
    DISTINCT
      T05.admission_date
      ,T05.member_dim_ck
      ,T05.external_member_id
      ,T05.plan_dim_ck
      ,T05.member_curr_ck
      ,T05.authorization_ck
      ,T05.event_reason_dim_ck
      ,T05.um_service_type_dim_ck
      ,T05.admission_source_dim_ck
      ,T05.attend_prov_aff_dim_ck
      ,T05.diagnosis_type
      ,T05.plan_type
      ,T05.member_amisys_nbr
      ,T05.sex
      ,T05.edw_member_ck
      ,T05.mpi_id
      ,T05.pro_generic_product_desc
      ,T05.diag_code
      ,T05.diag_desc
      ,T06.PTSD_COUNT
      ,T06.TRAUMA_COUNT
      ,T06.SELF_HARM_COUNT
      ,T06.SCHIZO_COUNT
      ,T06.OCD_COUNT
      ,T06.COVID19_COUNT
      ,T06.DEPRESSION_COUNT
      ,T06.ANXIETY_COUNT
      ,T06.DEMENTIA_COUNT
      ,T06.PARKINSONS_COUNT
      ,T06.BIPOLAR_COUNT
      ,T06.SUICIDTN_COUNT
      ,T06.SUICIDE_COUNT
      ,T06.PERS_DIS_COUNT
      ,T06.BPD_COUNT
      ,T06.CHRON_PAIN_COUNT
      ,T06.BH_COUNT
      ,BUPREN.BUPREN_CLAIMS BUPREN_COUNT
      ,NALOX.NALOXONE_CLAIMS NALOXONE_COUNT
      ,OPIOID.OPIOID_CLAIMS OPIOID_COUNT

      FROM #WANG_MEMS T05


        /*Aggregrate number of diags by member based on model run date*/
        LEFT JOIN (SELECT
                   T06.PLAN_DIM_CK
                   ,T06.MPI_ID
                   ,T05.admission_date
                   ,SUM(T06.PTSD) PTSD_COUNT
                   ,SUM(T06.TRAUMA) TRAUMA_COUNT
                   ,SUM(T06.SELF_HARM) SELF_HARM_COUNT
                   ,SUM(T06.SCHIZO) SCHIZO_COUNT
                   ,SUM(T06.OCD) OCD_COUNT
                   ,SUM(T06.COVID19) COVID19_COUNT
                   ,SUM(T06.DEPRESSION) DEPRESSION_COUNT
                   ,SUM(T06.ANXIETY) ANXIETY_COUNT
                   ,SUM(T06.DEMENTIA) DEMENTIA_COUNT
                   ,SUM(T06.PARKINSONS) PARKINSONS_COUNT
                   ,SUM(T06.BIPOLAR) BIPOLAR_COUNT
                   ,SUM(T06.SUICIDTN) SUICIDTN_COUNT
                   ,SUM(T06.SUICIDE) SUICIDE_COUNT
                   ,SUM(T06.PERS_DIS)PERS_DIS_COUNT
                   ,SUM(T06.BPD_DIS) BPD_COUNT
                   ,SUM(T06.CHRON_PAIN) CHRON_PAIN_COUNT
                   ,SUM(T06.BEHAVIORAL_HEALTH) BH_COUNT

                      FROM MANDA_OWN_TABLES.PYR8S_BH_DATA_T01 T06

                        /*Convert serv date to actual date*/
                        INNER JOIN ETL_ACCESS_OWN.DIM_DATE DD
                          ON T06.SERV_DATE = DD.DATE_DIM_CK

                        /*join so we can make sure serv date is < model run date*/
                        INNER JOIN #WANG_MEMS T05
                          ON T06.PLAN_DIM_CK = T05.PLAN_DIM_CK
                          AND T06.MPI_ID = T05.MPI_ID

                  WHERE DD.DATE_DATE <= T05.admission_date

                GROUP BY 1,2,3
                ) T06
          ON T05.PLAN_DIM_CK = T06.PLAN_DIM_CK
          AND T05.MPI_ID = T06.MPI_ID
          AND T05.admission_date = T06.admission_date


        LEFT JOIN #BUPRENORPHINE BUPREN
          ON T05.PLAN_DIM_CK = BUPREN.PLAN_DIM_CK
          AND T05.MPI_ID = BUPREN.MPI_ID
          AND T05.admission_date = BUPREN.admission_date

        LEFT JOIN #NALOXONE NALOX
          ON T05.PLAN_DIM_CK = NALOX.PLAN_DIM_CK
          AND T05.MPI_ID = NALOX.MPI_ID
          AND T05.admission_date = NALOX.admission_date

        LEFT JOIN #OPIOIDS OPIOID
          ON T05.PLAN_DIM_CK = OPIOID.PLAN_DIM_CK
          AND T05.MPI_ID = OPIOID.MPI_ID
          AND T05.admission_date = OPIOID.admission_date
)
WITH DATA
PRIMARY INDEX(PLAN_DIM_CK, MPI_ID, admission_date)
;

/********************************************************
Step 5. Adding flags for when the member was
        first diagnosed with a chronic condition
********************************************************/
CREATE VOLATILE TABLE #FIRST_CC_DIAG AS (
SELECT
PLAN_DIM_CK
,MPI_ID
,MIN(SERV_DATE) FIRST_CC_DIAG

FROM (
SELECT
DIAG.PLAN_DIM_CK
,T05.MPI_ID
,DIAG.CLAIM_NBR
,CC.CHRONIC_CONDITION
,MIN(SERV.SERVICE_START_DATE_DIM_CK) SERV_DATE

  FROM ETL_ACCESS_OWN.BRG_CLAIM_DIAGNOSIS DIAG

  /*Limit to only chronic condition diagnosis*/
  INNER JOIN POP_HEALTH_APP_OWN.CHRONIC_CONDITION_DX_DIMS CC
    ON DIAG.DIAG_CODE_DIM_CK = CC.DIAG_CODE_DIM_CK

   /*Pull claim date*/
  INNER JOIN ETL_ACCESS_OWN.FT_SERVICE_TRANSACTION SERV
    ON DIAG.CLAIM_NBR = SERV.CLAIM_NBR

INNER JOIN ETL_ACCESS_OWN.DIM_MEMBER_CURR MEM
  ON SERV.MEMBER_CURR_CK = MEM.MEMBER_CURR_CK
    AND SERV.PLAN_DIM_CK = MEM.PLAN_DIM_CK

  /*Limit to our Membership*/
  INNER JOIN #WANG_MEMS T05
    ON MEM.MPI_ID = T05.MPI_ID
    AND MEM.PLAN_DIM_CK = T05.PLAN_DIM_CK

GROUP BY 1,2,3,4
) A
GROUP BY 1,2
)
WITH DATA
PRIMARY INDEX(PLAN_DIM_CK, MPI_ID)
ON COMMIT PRESERVE ROWS;

/********************************************************
Step 6. Adding in actual flags to the dataset
********************************************************/

DROP TABLE MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL;

CREATE TABLE MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL AS (
  SELECT
    DISTINCT
      T07.admission_date
      ,T07.member_dim_ck
      ,T07.external_member_id
      ,T07.plan_dim_ck
      ,T07.member_curr_ck
      ,T07.authorization_ck
      ,T07.event_reason_dim_ck
      ,T07.um_service_type_dim_ck
      ,T07.admission_source_dim_ck
      ,T07.attend_prov_aff_dim_ck
      ,T07.diagnosis_type
      ,T07.plan_type
      ,T07.member_amisys_nbr
      ,T07.sex
      ,T07.edw_member_ck
      ,T07.mpi_id
      ,T07.pro_generic_product_desc
      ,T07.diag_code
      ,T07.diag_desc
      ,T07.ptsd_count
      ,T07.trauma_count
      ,T07.self_harm_count
      ,T07.schizo_count
      ,T07.ocd_count
      ,T07.covid19_count
      ,T07.depression_count
      ,T07.anxiety_count
      ,T07.dementia_count
      ,T07.parkinsons_count
      ,T07.bipolar_count
      ,T07.suicidtn_count
      ,T07.suicide_count
      ,T07.pers_dis_count
      ,T07.bpd_count
      ,T07.chron_pain_count
      ,T07.bh_count
      ,T07.bupren_count
      ,T07.naloxone_count
      ,T07.opioid_count
      ,CC.cc_diag_30_days
      ,CC.cc_diag_60_days
      ,CC.cc_diag_90_days
      ,SUI.suicide_prob
      ,IPR.orca_score
      ,IPR.sud_seg_value

  FROM MANDA_OWN_TABLES.PYR8S_BH_DATA_T02 T07

    /*Flagging time person first diagnosis occured*/
    LEFT JOIN (SELECT
                T05.plan_dim_ck
                ,T05.mpi_id
                ,T05.admission_date
                ,(CASE WHEN DD.date_date BETWEEN (T05.admission_date - 30) AND T05.admission_date
                      THEN 1
                ELSE 0 END) cc_diag_30_days
                ,(CASE WHEN DD.date_date BETWEEN (T05.admission_date - 60) AND T05.admission_date
                      THEN 1
                ELSE 0 END) cc_diag_60_days
                ,(CASE WHEN DD.date_date BETWEEN (T05.admission_date - 90) AND T05.admission_date
                      THEN 1
                ELSE 0 END) cc_diag_90_days

                  FROM #WANG_MEMS T05

                  LEFT JOIN #FIRST_CC_DIAG CC
                    ON T05.plan_dim_ck = CC.plan_dim_ck
                    AND T05.mpi_id = CC.mpi_id

                  INNER JOIN ETL_ACCESS_OWN.DIM_DATE DD
                    ON CC.first_cc_diag = DD.date_dim_ck
      ) CC
        ON T07.PLAN_DIM_CK = CC.plan_dim_ck
        AND T07.MPI_ID = CC.mpi_id
        AND T07.admission_date = CC.admission_date

    /*Get suicide probability scores*/
    LEFT JOIN (select 
               mpi_id, 
               plan_dim_ck, 
               suicide_prob, 
               model_run_date
               from DATA_SCI_APP_OWN.HCA_DS_CLN_SUIC_OUTPUT
               qualify row_number() over (partition by mpi_id, plan_dim_ck order by model_run_date desc ) = 1
               ) as SUI
    ON T07.plan_dim_ck = SUI.plan_dim_ck AND T07.mpi_id = SUI.mpi_id

    /*get ipro risk scores*/
    LEFT JOIN (SELECT
               ab.admission_date,
               m.edw_member_ck,
               iprom.sud_seg_value,
               iprom.orca_score,
               iprom.publish_date
            FROM etl_access_own.ft_authorization AS ab
            JOIN etl_access_own.dim_plan AS p
            ON ab.plan_dim_ck = p.plan_dim_ck
            JOIN etl_access_own.dim_member AS m
            ON ab.member_dim_ck = m.member_dim_ck
            left join etl_access_own.dim_ipro_member as iprom
            on m.edw_member_ck = iprom.edw_member_ck and ab.admission_date > iprom.publish_date
            WHERE ab.admission_date BETWEEN '2021-01-01 00:00:00' AND '2023-04-01 00:00:00'
            AND iprom.publish_date BETWEEN '2021-01-01 00:00:00' AND '2023-04-01 00:00:00'
            AND ab.external_member_id IS NOT NULL -- cannot join if either admission_date or member_id is null
            AND ab.admission_date IS NOT NULL -- since a visit is defined as a unique admit_date and member_id
            AND p.plan_dim_ck IN (41,62,68,82,83,108,127,109,130,132,213,44,69,45,51,126,107,105,110,106,
           104,203,202,201,204,205,76,102,1,101,103,73,21,2,26,125,12,15,20,61,32,115,49,59,23,14,50,55,
           117,146,124,128,54,118,22,10,27,60,37,70,122,112,228,223,114,123,138,140,136,5,121,16,57,143,
           144,145,209,210,211,212,226,39,119,75,40,4,137,74,46)
            AND left(ab.auth_nbr, 2) NOT IN ('OP', 'OB')
          QUALIFY ROW_NUMBER() OVER (PARTITION BY m.edw_member_ck, ab.admission_date ORDER BY iprom.publish_date DESC) = 1
            ) AS IPR
  ON T07.edw_member_ck = IPR.edw_member_ck AND T07.admission_date = IPR.admission_date
)
WITH DATA
PRIMARY INDEX(plan_dim_ck, mpi_id, admission_date);


SELECT COUNT(*) FROM #WANG_MEMS;

select Top 1000 * from MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL;

select count(*) from MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL;
select count(bupren_count) from MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL;
select count(NALOXONE_COUNT) from MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL;
select count(OPIOID_COUNT) from MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL;


select admission_date
      ,external_member_id
      ,member_amisys_nbr
      ,ptsd_count
      ,trauma_count
      ,self_harm_count
      ,schizo_count
      ,ocd_count
      ,covid19_count
      ,depression_count
      ,anxiety_count
      ,dementia_count
      ,parkinsons_count
      ,bipolar_count
      ,suicidtn_count
      ,suicide_count
      ,pers_dis_count
      ,bpd_count
      ,chron_pain_count
      ,bh_count
      ,bupren_count
      ,naloxone_count
      ,opioid_count
      ,cc_diag_30_days
      ,cc_diag_60_days
      ,cc_diag_90_days
      ,suicide_prob
      ,orca_score
      ,sud_seg_value
from MANDA_OWN_TABLES.PYR8S_BH_DATA_FINAL;