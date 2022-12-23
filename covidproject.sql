/*
Data Exploration of Covid
*/

Select *
From covid.deaths
order by location;


-- Select Data that we are starting with India, china, Malaysia, Singapore, Srilanka, Qatar, Saudi Arabia
-- Date wise Number of cases & deaths 

Select continent, location, date, new_cases, new_deaths
From covid.deaths
Where location in ('india', 'china', 'malaysia','singapore', 'sri lanka', 'qatar','saudi arabia')
Order by location; 


-- Creating View to store data for later visualizations

Create View Casesanddeath as
Select continent, location, date, new_cases, new_deaths
From covid.deaths
Where location in ('india', 'china', 'malaysia','singapore', 'sri lanka', 'qatar','saudi arabia')
Order by location;


-- Total Cases vs Total Deaths

Select location, SUM(new_cases) as Totalcases, SUM(new_deaths) as Totaldeaths From covid.deaths
group by location
order by location;


-- Total Cases vs Total Deaths
-- Countries with Death Percentge 

Select location, SUM(new_cases) as Totalcases, SUM(new_deaths) as Totaldeaths, 
(SUM(new_deaths)/SUM(new_cases))*100 as DeathPercentage From covid.deaths
group by location
order by DeathPercentage Desc;


-- Total Cases vs Total Deaths
-- Continent wise Death Percentge 

SELECT continent, SUM(new_cases) as Totalcases, SUM(new_deaths) as Totaldeaths, 
(SUM(new_deaths)/SUM(new_cases))*100 as DeathPercentage From covid.deaths
group by continent
order by DeathPercentage Desc;


-- Total Cases vs Population 
-- Asia Continent Highest Percentage of Totalcases/Population 

Select Location, date, Population, sum(new_cases) as Totalcases,  (sum(new_cases)/population)*100 as PercentPopulationInfected
From covid.deaths
Where continent='asia'
group by location
order by PercentPopulationInfected DESC;


-- Continent with Highest Percentage of Totalcases/Population 

Select continent, sum(new_cases) as Totalcases, population, (sum(new_cases)/population)*100 as PercentPopulationInfected
From covid.deaths
Group by continent
order by PercentPopulationInfected DESC;


-- Total Death vs Population 
-- Countries with Highest Percentage of Totaldeaths/Population 

Select continent, location, sum(new_deaths) as Totaldeaths, population
From covid.deaths
Group by location
order by location;

-- Using CTE to perform Calculation on DeathPercentage in previous query

With Totaldeaths as(
Select continent,location, sum(new_deaths) as Totaldeaths, population
From covid.deaths
Group by location
order by 1,2)
Select *, (Max(Totaldeaths)/population)*100 as DeathPercentage
From Totaldeaths
Group by location
order by DeathPercentage DESC;


-- Global Totalcases, Totaldeaths, Deathpercentage

Select SUM(new_cases) as Totalcases, SUM(new_deaths) as Totaldeaths, 
(SUM(new_deaths)/SUM(new_cases))*100 as DeathPercentage From covid.deaths
-- group by location
 order by 1,2;


-- Total Population vs Vaccinations in India

Select covid.deathcovid.continent, covid.deaths.location, covid.deathcovid.population, 
max(covid.vaccination.people_vaccinated) as Peoplevaccinationindia
 From ((covid.deaths 
inner join covid.deathcovid on covid.deaths.location = covid.deathcovid.location)
inner join covid.vaccination on covid.deathcovid.date=covid.vaccination.date)
where covid.deathcovid.location='india'
group by covid.deathcovid.location
order by 1,2;

-- Shows Percentage of Population that has recieved at least one Covid Vaccine

Select covid.deathcovid.continent, covid.deaths.location, covid.deathcovid.population, 
max(covid.vaccination.people_vaccinated) as Peoplevaccinationindia, 
(max(covid.vaccination.people_vaccinated)/covid.deathcovid.population)*100 as Vaccinatepercentageindia
 From ((covid.deaths 
inner join covid.deathcovid on covid.deaths.location = covid.deathcovid.location)
inner join covid.vaccination on covid.deathcovid.date=covid.vaccination.date)
where covid.deathcovid.location='india'
group by covid.deathcovid.location
order by 1,2;






